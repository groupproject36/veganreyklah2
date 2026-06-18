# 998 · The Rye Almanac

*A growing reference of how Rye and its Zig 0.16.0 toolchain actually work — each entry earned by running code, recorded so the next builder need not rediscover it.*

**Language:** EN
**Version:** `20260617.194312` (Rye chronological stamp)
**Last updated:** 2026-06-17
**Style:** Radiant (see `../context/RADIANT_STYLE.md`); code in TAME Style (`../external-research/996_TAME_STYLE.md`)
**Status:** Living

---

## What the Almanac Holds

This is the field reference for building Rye. Every entry below was confirmed by code that compiled and ran, on the prebuilt Zig 0.16.0 toolchain we keep at `vendor/zig-toolchain`. When the toolchain's standard library surprised us — and the move to its new I/O model surprised us often — we wrote the truth down here, plainly, so the surprise becomes settled knowledge.

Read it as an almanac: practical, accumulated, seasonal. It grows as Rye grows.

---

## Rye v1 Stands on the Zig Toolchain

Rye's first version is honest about what it is: a thin front-end over the Zig 0.16.0 toolchain. A `.rye` file is Zig source for now, since the language has yet to diverge, so every capability the toolchain offers is Rye's by construction.

The one wrinkle we met immediately: the toolchain's front-end reads only the `.zig` extension. `zig run file.rye` answers `error: unrecognized file extension`. So the `rye` command bridges — it copies the `.rye` source to an adjacent `.zig` file, hands that to the compiler, and clears the bridge away afterward so the tree stays tidy. A single-file run needs nothing more.

---

## The Entry Point: the Init Handshake

Zig 0.16.0 changed how a program begins, and the change is a gift to clarity. A `main` function may now accept one argument, `std.process.Init`, and the runtime hands it everything a program needs, explicitly, rather than through hidden globals:

- `init.minimal.args` — the command-line arguments.
- `init.minimal.environ` — the environment.
- `init.arena` — a process-wide arena allocator, cleared automatically on exit.
- `init.gpa` — a general-purpose allocator for finer-grained, freed-as-you-go work.
- `init.io` — the I/O implementation, threaded explicitly through every operation that touches the outside world.
- `init.environ_map` — the environment parsed into a lookup map.
- `init.preopens` — files handed down by the parent process.

`main` may return `void`, `!void`, `noreturn`, `u8`, or `!u8`. Returning `!u8` is the clean way to give an exit code: the value flows straight out as the process's status, with no separate exit call needed.

---

## Arguments and the Environment

The familiar `argsAlloc` is gone. Arguments now arrive through the `Init` handshake and become a slice with one call:

- `const args = try init.minimal.args.toSlice(allocator);` yields `[]const [:0]const u8`.

Environment lookups are equally direct, through the parsed map:

- `const value = init.environ_map.get("RYE_ZIG");` yields `?[]const u8`.

The `rye` command uses exactly these: the first to read its subcommand and file, the second to find its toolchain through the `RYE_ZIG` variable.

---

## The I/O Model: `io`, Threaded Explicitly

The largest change in 0.16.0 is that input and output flow through an explicit `io` value rather than ambient global state. This is deeply in the spirit we already keep: nothing reaches the outside world by surprise; the capability is passed, plainly, to whatever uses it.

In practice this means the old `std.fs` is now a deprecated doorway to `std.Io.Dir`, and the filesystem calls take `io`:

- `const dir = std.Io.Dir.cwd();` — open the current directory (no `io` needed for this one).
- `dir.readFileAlloc(io, sub_path, allocator, limit)` — read a whole file; `limit` may be `.unlimited`.
- `dir.writeFile(io, .{ .sub_path = path, .data = bytes })` — write a file.
- `dir.deleteFile(io, sub_path)` — remove one.

Path helpers such as `std.fs.path.basename` still work; they are pure string work and need no `io`. And `std.debug.print` still takes the familiar format strings — `{s}` for a string, `{d}` for a number — which kept our diagnostics simple. For an error value, `@errorName(err)` with `{s}` prints its name reliably.

---

## Spawning the Toolchain

The `rye` command runs a `.rye` file by handing the bridged `.zig` to the toolchain as a child process. The spawn likewise takes `io`:

- `var child = try std.process.spawn(io, .{ .argv = argv });` — `argv` is `[]const []const u8`, its first element the program to run.
- `const term = try child.wait(io);` — wait for completion, yielding a `Term`.

A `Term` reports how the child ended: `.exited` carries a `u8` status, and `.signal`, `.stopped`, and `.unknown` cover the rest. The `rye` command returns the child's `.exited` code as its own, so a failing `.rye` program surfaces its failure honestly.

A small kindness in the defaults: the child's standard input, output, and error all `inherit` from the parent unless asked otherwise, so a program's output streams straight to the terminal with no plumbing on our part. When `argv[0]` holds a path with a slash, it is run as that path; otherwise it is resolved through the parent's PATH. We pass an absolute toolchain path through `RYE_ZIG`, so the backend in use is never in doubt.

---

## Memory, the Tally Way

The first run of the `rye` command worked and printed the right answer — and the debug allocator then reported several leaks. The lesson was clean and on-theme. We had allocated from `init.gpa`, the leak-checking general allocator, and never freed, so it rightly complained.

The fix is the region model we already cherish, here named Tally in our designs: allocate a short-lived command's memory from `init.arena.allocator()`. The arena is one garden, cleared whole by the runtime on exit, so there is nothing to track and nothing to leak. Switching the command's allocations to the arena turned a noisy run into a silent, clean one. The guidance settles simply: for whole-command, live-until-exit allocations, reach for the arena; reserve the freed-as-you-go allocator for memory with a shorter, finer lifetime.

---

## SHA3-512 Parity

The first thing we asked Rye to prove was that SHA3-512 works exactly as it does in Zig 0.16.0. It does, by the only honest measure: a known-correct digest, matched.

The standard library offers `std.crypto.hash.sha3.Sha3_512`, with a `digest_length` of 64 bytes and a one-call form, `Sha3_512.hash(message, &digest, .{})`. We hashed the bytes `"Rye"`, rendered the digest as lowercase hex by hand, and asserted it against a digest computed independently beforehand. It matched to the last nibble:

```
SHA3-512("Rye") = c692f0476279e6b867ee66c6701c119106a38f46881da52d733ac2b0cd092e96
                  30249106dba551524678e70cea61686016926bdc984a191d055b329f2336763f
```

Because Rye v1 is the toolchain under a new name, this is not an approximation of Zig's cryptography — it is the very same code, confirmed.

---

## Building and Running

Two paths, both confirmed:

- **The toolchain.** We fetched the official prebuilt Zig 0.16.0 release, verified its SHA-256 against the published sum before trusting a byte, and keep it at `vendor/zig-toolchain`. Verifying the artifact before use is the safe habit, and it cost nothing.
- **The build.** `zig build-exe rye/src/main.zig -femit-bin=rye/bin/rye` produces the `rye` command directly. With the toolchain on hand, `rye run rye/tests/sha3_512_test.rye` compiles and runs the test, printing the digest and confirming parity.

---

## Open Threads

A few paths we have left lit for later, each a deliberate choice rather than an oversight:

- **Self-hosting the `rye` command.** For now it is a small Zig program. As Rye finds its own shape, the command can be written in Rye itself — the natural end state.
- **A `build.rye` story.** Zig builds projects through a `build.zig` script; Rye will want its own `build.rye`, bridged the same way single files are today.
- **A bounded read.** The command reads a source file with an unlimited size; a future version can bound it, in keeping with putting a limit on everything.
- **Many-file programs.** The single-file bridge serves the first version; multi-file `.rye` projects, with their imports, are a thread to pick up next.

---

*May each finding here stay true, and may the next builder trust it. May the gardens we allocate clear cleanly, the digests we compute match to the last nibble, and the language we grow stand surely on ground we have tested ourselves.*

