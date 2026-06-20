# 995 · Open Threads — The System Takes Shape

*A living snapshot of what has landed, what is closed, and what remains open. Updated at `172012`: pass 9963 `SplitIterator.first`; corpus 40.*

**Language:** EN
**Version:** `20260620.172012` (Rye chronological stamp)
**Last updated:** 2026-06-20
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Voice:** Reya 2

---

## What Just Landed (this session)

- **Strengthening pass 9963 (`172012`).** `SplitIterator.first` postconditions; corpus 40/40 GREEN.
- **Strengthening pass 9964 (`171512`).** `findLastNone` postconditions; corpus 39 GREEN.
- **Strengthening pass 9965 (`171112`).** `findNonePos` + `findNone` postconditions; corpus 38 GREEN.
- **Strengthening pass 9966 (`170312`).** `findLastAny` postconditions; corpus 37 GREEN.
- **Strengthening pass 9967 (`165812`).** `findAnyPos` + `findAny` postconditions; corpus 36 GREEN.
- **Strengthening pass 9968 (`165512`).** `SplitIterator.rest`; corpus 35 GREEN.
- **Strengthening pass 9969 (`165112`).** `SplitIterator.peek`; corpus 34 GREEN.
- **Strengthening pass 9970 (`164812`).** `std.mem.findLast`; corpus 33 GREEN.
- **Strengthening pass 9971 (`164312`).** `std.mem.findPos`; corpus 32 GREEN.
- **Strengthening pass 9972 (`164012`).** `std.mem.findLastLinear`; corpus 31 GREEN.
- **Strengthening pass 9973 (`163512`).** `std.mem.findPosLinear`; corpus 30 GREEN.
- **Strengthening pass 9974 (`163112`).** `std.mem.findScalarPos`; corpus 29 GREEN.
- **Strengthening pass 9975 (`162712`).** `std.mem.findScalarLast`; corpus 28 GREEN.
- **Strengthening pass 9976 (`161812`–`162512`).** `std.fs.path.stem`; corpus 27 GREEN.
- **Strengthening pass 9977 (`161312`).** `std.fs.path.extension` postcondition; corpus 26/26 GREEN.
- **Garden-memory policy (`161112`–`161312`).** Authored `.rye` never uses `ArenaAllocator` directly — use `init.garden.allocator()`. No `std.heap.GardenAllocator` rename; owned wrapper path is `rye.garden` / `tally/heap-garden.rye`. Recorded in `inherited-names.md`, `tame-style.md`, `.cursor/rules/tame-style.mdc`, `.claude/rules/tame-style.md`.
- **Strengthening pass 9978 (`160312`).** `std.fs.path.basename`; corpus 25/25 GREEN.
- **Living docs refresh (`160312`).** `994_style_audit.md` (timestamp removed from filename); `995` and `996` brought current after `155212` ship.
- **Style audit shipped (`155212`).** TAME + Radiant GREEN on 22 `.rye`/`.rish` files; record at `work-in-progress/994_style_audit.md`. Seven commits pushed to all remotes (`36203a9`).
- **Strengthening 9979–9987 (`143312`–`050912`).** `trimStart`, `path.dirname`, `process.run`, `allocPrint`+`trimEnd`, `path.join`, `readFileAlloc`, `writeStreamingAll`, `bufPrint`, `Allocator.alloc` + Skate `.rye` migration — corpus grew 17 → 24.
- **Rishi builtins + parser (`151212`–`153812`).** `split`, `join`, `ends-with`, string `contains`, infix `index-of`; `findComparison` before infix word ops; `isWordHyphen` for hyphenated identifiers vs subtraction. Rishi stamp `20260620.153812`.
- **Parity via `rye run` (`145612`).** Corpus `.rye` through `rye run`; baseline arm `RYE_LIB=vendor/zig-toolchain/lib`.
- **Skate text grid.** Monospace 8×8 glyphs on Wayland; headless `selftest` green.

## Threads Now Closed

- **Crypto foundation** — AEAD, SHA3-512, Ed25519, X25519. Parity-green, hosted and freestanding.
- **Sealed datagram** — `posted.rye`: two harts, shared-memory mailbox.
- **`parity.rish`** — the gate in our own shell, GREEN and RED.
- **Rishi arithmetic + stdout** — `+`/`-`/`*`/`/`, correct precedence, `say`.
- **Tally seed** — one Region, 13 invariants.
- **Tally v1 named gardens** — `Gardens`, blob/diff/frame, 15/15 GREEN.
- **Strengthening 9994–9963** — through `SplitIterator.first`. Corpus 40.
- **Mantra seed** — weave, LCS diff, SHA3-256 store, init/add/status.
- **Mantra for the repo (seed)** — commit chain, add-all walks `.brix`, log follows chain. 9/9 bricks.
- **`init.garden` (phase 1)** — `std.process.Init.garden` renamed from upstream `arena`.
- **Garden-memory policy** — authored code uses `init.garden`, never `ArenaAllocator`; no std `GardenAllocator` alias; TAME + Cursor + Claude rules.
- **Brix minimum** — `.brix` descriptor, 10 tracked bricks.
- **Rishi file I/O** — `read-file`, `write-file`, `list-dir`.
- **Rishi string builtins** — `length`, `trim`, `slice`, `lines`, `starts-with`, `ends-with`, `split`, `join`, `contains`, infix `index-of`.
- **Rishi parser hyphen fix** — comparisons before infix words; `isWordHyphen`.
- **Caravan seed** — parent/child restart, 5 assertions.
- **Caravan bounded** — supervision + Tally garden, 10 assertions.
- **Aurora deciding stage** — wake, prove, decide, rest.
- **`additive-gate.rish`** — gate trio complete in Rishi. `.sh` fallbacks removed.
- **`parity-selftest.rish`** — the gate proves RED.
- **Brix + Tablecloth naming** — compose (Brix) vs store (Tablecloth) vs discipline (silo/siloed); prompt ladder `10018`–`10022`.
- **TAME Style spec** — `context/specs/tame-style.md` + Claude rule.
- **GPL compliance** — gitlinks, River not cloned, clean-room boundary.
- **Formats, editors, inference research (`970`).**
- **Horizon modules siloed (`978`).** Scribble, Lantern, Lattice, Anvil.
- **Flow of values foundation (`977`).**
- **Seed vocabulary (`976`).**
- **Brushstroke Wayland seed.** Native window, one frame from values.
- **Caravan multi-child (twin seed).** Two supervised children, independent gardens.
- **Caravan chain-loading (`caravan/chain.rye`).**
- **Comlink hosted wire (`comlink/hosted_wire.rye`).**
- **Skate text grid.** Monospace 8×8 glyphs on `wayland_seed`; headless `selftest` green.
- **Style audit (`155212`).** TAME + Radiant GREEN; record `994_style_audit.md`.

## Threads Still Open

**Main track — Rye · Rishi · strengthening:** `expanding-prompts/10023_main_track_rye_rishi_strengthening.md` (`044412`). Run this for the current build order; `10010` is a reserved stub only.

| Priority | Thread | Anchor |
|----------|--------|--------|
| 1 | **Strengthening series** — next `std` surface through gate trio (9962 and below) | `10023` Track B, `998` |
| 2 | **Rishi** — builtins as gates and Pond policy need them | `10023` Track C |
| 3 | **TAME assertion backlog** — fix as code is touched | `994_style_audit.md` |

**Near — build (after main track holds green):**

- **Device wire (virtio-net)** — sealed datagram over emulated link (`10016`).
- **Caravan capability table** — small Rye struct per child (`984` step 5).

**Documented — Tablecloth (deferred code, ladder ready):**

- **`10018`–`10022`** — vocabulary, Brix split, build contract, value model, v1 seed spec.
- **Tablecloth v1** — grow from `.mantra/blobs/` when Rye/Rishi/strengthening stay on track (`10022`, `996` Horizon 2). Prose and prompts are unified; implementation waits.

**Near — study:**

- **Display-layer study** — Wayland specs for Brushstroke; Ghostty (MIT) for Skate.
- **Close reading** — packet format, commit rule, relay protocols from `gratitude/`.
- **TAME editor design** — select-then-act, Brix settings, Rishi behavior (`971`, `980`).
- **JSON unified with Brix** — one value grammar (`970`, `978`).
- **Comlink remoting** — value-based state sync (`971`).

**Horizon 2:**

- **Pond GUI** — Rishi REPL + Mantra in a Brushstroke window (`10009`, `986`).
- **The Forge** — Mantra-native forge (`982`).
- **Brix v1** — lawful combinator over brick descriptors (`10019`, `10020`).
- **Tally-native `garden` module** — `rye/lib/rye/garden.zig` or `tally/heap-garden.rye`: owned wrapper beside inherited `ArenaAllocator`; graduates to native Tally (`inherited-names.md`, `9989`).

**Horizon — inference & tensors** *(see `978`):* Lantern, Lattice, Anvil.

**Ongoing — design:**

- **`pond.rish`** — enclosure as a value.
- **Owner-key PKI** — rotation, revocation, recovery.
- **Verify-flag hot path** — data-plane postconditions.

**Ongoing — Rye vocabulary (`.rye` vs `.zig`):**

| Layer | Extension | Role |
|-------|-----------|------|
| **Our programs** | `.rye` | Rishi, seeds, Skate, corpus tests — what we author |
| **Our std** | `.zig` under `rye/lib/std` | Strengthened surfaces the compiler reads via `--zig-lib-dir` |
| **Ephemeral bridge** | adjacent `.zig` | `rye run` / `rye build` only; deleted after compile |

Skate briefly used `.zig` modules; migrated at `050912` with recursive `.rye` import bridging. **Whole std as `.rye`** is a horizon move — the lib tree is the backend layout today.

**Garden naming — where we stand:**

| Layer | Status |
|-------|--------|
| `std.process.Init.garden` | Done (phase 1) |
| Locals in rye/rishi/benchmarks/docs | Done (phase 2) |
| Authored `.rye` / `.rish` | `init.garden` only — never `ArenaAllocator` (TAME rule) |
| `ArenaAllocator` in inherited std | Keep — do not rename to `GardenAllocator` |
| Owned wrapper | Horizon — `rye.garden` / `tally/heap-garden.rye` |
| Upstream std internals / vendor | Untouched |

Phase 2 vocabulary sweep is **closed**. Policy at `161112`: warm names enter beside inherited types, not as renames.

**Parity contract (`145612`):**

- **Compare:** baseline `vendor/zig-toolchain/lib` vs strengthened `rye/lib` — same test, same pinned Zig (`RYE_ZIG`).
- **Invoke:** `rye run rye/tests/<name>.rye` on both arms (`RYE_LIB` for baseline); exercises the real bridge path.
- **Hold:** exit code + stdout/stderr identical — assertions change what code *says*, never what it *does*.
- **Corpus:** 40 programs, all GREEN (9963 `SplitIterator.first` latest).

## The Through-Line

One value model, all the way down. The main work now is **Rye** growing surely, **Rishi** scripting the gates, and **strengthening** earning each `std` surface before the next layer composes. Garden memory in authored code flows through `init.garden`; inherited `ArenaAllocator` stays in std until `rye.garden` earns its keep. Tablecloth's ladder waits documented on the side.

---

*May the threads stay visible while they are open, and be tied off honestly when they close.*
