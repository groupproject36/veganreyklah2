# 995 · Open Threads — The System Takes Shape

*A living snapshot of what has landed, what is closed, and what remains open. Updated at `205212`: pass 9934 mem split factories; 69 witnesses.*

**Language:** EN
**Version:** `20260620.205212` (Rye chronological stamp)
**Last updated:** 2026-06-20
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Voice:** Reya 2

---

## What Just Landed (this session)

- **Strengthening pass 9934 (`205212`).** `splitScalar` / `splitAny` / `splitSequence` factory postconditions; witness `mem_split_factory_test`; 69/69 witnesses GREEN.
- **Strengthening pass 9935 (`204212`).** SHA3 `ShakeLike.squeeze` buffered `@memcpy` slice bounds in `sha3.zig`; witness `sha3_shake_buffered_memcpy_test`; 68/68 witnesses GREEN.
- **Strengthening pass 9936 (`203912`).** Keccak sponge `absorb` + `squeeze` `@memcpy` slice bounds in `keccak_p.zig`; witness `keccak_sponge_memcpy_test`; 67/67 witnesses GREEN.
- **Strengthening pass 9937 (`203612`).** `crypto.timing_safe.eql` postconditions; 66/66 witnesses GREEN.
- **Strengthening pass 9938 (`201912`).** `mem.endsWith` return-path postconditions; 65/65 witnesses GREEN.
- **Aurora metal lane documented (`200312`).** Parallel priority beside main mem arc; prefix/suffix pair now complete (`9938`–`9939`).
- **Strengthening pass 9939 (`200012`).** `mem.startsWith` return-path postconditions; 64/64 witnesses GREEN.
- **Strengthening pass 9940 (`195612`).** `mem.allEqual` postconditions; 63/63 witnesses GREEN.
- **Strengthening pass 9941 (`195412`).** `mem.eql` return-path postconditions; 62/62 witnesses GREEN.
- **Strengthening pass 9942 (`195112`).** `mem.len` postconditions; 61/61 witnesses GREEN.
- **Strengthening pass 9943 (`194512`).** `mem.copyForwards` postconditions; 60/60 witnesses GREEN.
- **Strengthening pass 9944 (`194012`).** `mem.copyBackwards` postconditions; 59/59 witnesses GREEN.
- **Strengthening pass 9945 (`193612`).** `mem.sliceTo` + `lenSliceTo` postconditions; 58/58 witnesses GREEN.
- **Strengthening pass 9946 (`193212`).** `SemanticVersion.format` postconditions; 57/57 witnesses GREEN.
- **Strengthening pass 9947 (`192712`).** `SemanticVersion.parse` + `parseNum` postconditions; 56/56 witnesses GREEN.
- **Strengthening pass 9948 (`192412`).** `SemanticVersion.order` + `Range` postconditions; 55/55 witnesses GREEN.
- **Strengthening pass 9949 (`191212`).** `findDiff` postconditions; 54 witnesses GREEN.
- **Strengthening pass 9950 (`185712`).** `containsAtLeast` + `containsAtLeastScalar2` postconditions; 53 witnesses GREEN.
- **Strengthening pass 9951 (`184712`).** `mem.count` + `countScalar` postconditions; 52 witnesses GREEN.
- **Strengthening pass 9952 (`184412`).** `orderZ` + `findSentinel` postconditions; 51 witnesses GREEN.
- **Strengthening pass 9953 (`182812`).** `mem.order` + `lessThan` postconditions; 50 witnesses GREEN.
- **Strengthening pass 9954 (`181512`).** `WindowIterator` postconditions; 49 witnesses GREEN.
- **Strengthening pass 9955 (`180712`).** iterator `reset` postconditions; 48 witnesses GREEN.
- **Strengthening pass 9956 (`180012`).** `TokenIterator.next` postconditions; 47 witnesses GREEN.
- **Strengthening pass 9957 (`175712`).** `TokenIterator.peek` + `rest` postconditions; 46 witnesses GREEN.
- **Strengthening pass 9958 (`175312`).** `cutLast` + `cutScalarLast` postconditions; 45 witnesses GREEN.
- **Strengthening pass 9959 (`174912`).** `cut` + `cutScalar` postconditions; 44 witnesses GREEN.
- **Strengthening pass 9960 (`174312`).** `cutPrefix` + `cutSuffix` postconditions; 43 witnesses GREEN.
- **Strengthening pass 9961 (`173212`).** `mem.join` postconditions; 42 witnesses GREEN.
- **Strengthening pass 9962 (`172612`).** `SplitBackwardsIterator` postconditions; 41 witnesses GREEN.
- **Strengthening pass 9963 (`172012`).** `SplitIterator.first` postconditions; 40 witnesses GREEN.
- **Strengthening pass 9964 (`171512`).** `findLastNone` postconditions; 39 witnesses GREEN.
- **Strengthening pass 9965 (`171112`).** `findNonePos` + `findNone` postconditions; 38 witnesses GREEN.
- **Strengthening pass 9966 (`170312`).** `findLastAny` postconditions; 37 witnesses GREEN.
- **Strengthening pass 9967 (`165812`).** `findAnyPos` + `findAny` postconditions; 36 witnesses GREEN.
- **Strengthening pass 9968 (`165512`).** `SplitIterator.rest`; 35 witnesses GREEN.
- **Strengthening pass 9969 (`165112`).** `SplitIterator.peek`; 34 witnesses GREEN.
- **Strengthening pass 9970 (`164812`).** `std.mem.findLast`; 33 witnesses GREEN.
- **Strengthening pass 9971 (`164312`).** `std.mem.findPos`; 32 witnesses GREEN.
- **Strengthening pass 9972 (`164012`).** `std.mem.findLastLinear`; 31 witnesses GREEN.
- **Strengthening pass 9973 (`163512`).** `std.mem.findPosLinear`; 30 witnesses GREEN.
- **Strengthening pass 9974 (`163112`).** `std.mem.findScalarPos`; 29 witnesses GREEN.
- **Strengthening pass 9975 (`162712`).** `std.mem.findScalarLast`; 28 witnesses GREEN.
- **Strengthening pass 9976 (`161812`–`162512`).** `std.fs.path.stem`; 27 witnesses GREEN.
- **Strengthening pass 9977 (`161312`).** `std.fs.path.extension` postcondition; 26/26 witnesses GREEN.
- **Garden-memory policy (`161112`–`161312`).** Authored `.rye` never uses `ArenaAllocator` directly — use `init.garden.allocator()`. No `std.heap.GardenAllocator` rename; owned wrapper path is `rye.garden` / `tally/heap-garden.rye`. Recorded in `inherited-names.md`, `tame-style.md`, `.cursor/rules/tame-style.mdc`, `.claude/rules/tame-style.md`.
- **Strengthening pass 9978 (`160312`).** `std.fs.path.basename`; 25/25 witnesses GREEN.
- **Living docs refresh (`160312`).** `994_style_audit.md` (timestamp removed from filename); `995` and `996` brought current after `155212` ship.
- **Style audit shipped (`155212`).** TAME + Radiant GREEN on 22 `.rye`/`.rish` files; record at `work-in-progress/994_style_audit.md`. Seven commits pushed to all remotes (`36203a9`).
- **Strengthening 9979–9987 (`143312`–`050912`).** `trimStart`, `path.dirname`, `process.run`, `allocPrint`+`trimEnd`, `path.join`, `readFileAlloc`, `writeStreamingAll`, `bufPrint`, `Allocator.alloc` + Skate `.rye` migration — witnesses grew 17 → 24.
- **Rishi builtins + parser (`151212`–`153812`).** `split`, `join`, `ends-with`, string `contains`, infix `index-of`; `findComparison` before infix word ops; `isWordHyphen` for hyphenated identifiers vs subtraction. Rishi stamp `20260620.153812`.
- **Parity via `rye run` (`145612`).** Witness `.rye` through `rye run`; baseline arm `RYE_LIB=vendor/zig-toolchain/lib`.
- **Skate text grid.** Monospace 8×8 glyphs on Wayland; headless `selftest` green.

## Threads Now Closed

- **Crypto foundation** — AEAD, SHA3-512, Ed25519, X25519. Parity-green, hosted and freestanding.
- **Sealed datagram** — `posted.rye`: two harts, shared-memory mailbox.
- **`parity.rish`** — the gate in our own shell, GREEN and RED.
- **Rishi arithmetic + stdout** — `+`/`-`/`*`/`/`, correct precedence, `say`.
- **Tally seed** — one Region, 13 invariants.
- **Tally v1 named gardens** — `Gardens`, blob/diff/frame, 15/15 GREEN.
- **Strengthening 9994–9934** — through mem split factories. 69 witnesses.
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
| 1 | **Strengthening series** — next `std` surface through gate trio (9933 and below) | `10023` Track B, `998` |
| 2 | **Rishi** — builtins as gates and Pond policy need them | `10023` Track C |
| 3 | **TAME assertion backlog** — fix as code is touched | `994_style_audit.md` |
| 4 | **Aurora metal lane** — std surfaces on the freestanding crypto path (see below) | `991`, `9995`, `998` |

**Aurora metal lane** *(opened `200312`)* — parallel to the main mem/string arc, not a fork of it. Aurora's freestanding stages (`aurora/src/*.rye`, `riscv64-freestanding-none`) lean on **crypto** and a thin **mem** slice, not `std.os` or hosted I/O.

| Surface | Aurora / RISC-V role | Strengthening status |
|---------|---------------------|-------------------|
| `crypto.hash.sha3` + Keccak sponge | `named`, `sealed`, `posted` content-names and seal keys | **Done** — witnesses + sponge invariants (`9994`–`9998`) |
| `crypto.sign.Ed25519`, `dh.X25519`, `aead` ChaCha20-Poly1305 | Full sealed datagram on bare metal | **Done** — hosted witnesses; same `std` on RISC-V build |
| `mem.eql` | Content-name check in `sealed` / `posted` | **Done** (`9941`); **scalar path** is what RISC-V uses (`stage2_riscv64` disables vector `eqlBytes`) |
| `mem.copyForwards` / `copyBackwards` | Sibling discipline to sponge `@memcpy` buffer walks | **Done** (`9943`–`9944`) |
| `mem.startsWith` / `endsWith` | Mantra weave edges; `rye` suffix checks (hosted) | **Done** (`9938`–`9939`) |
| `crypto.timing_safe.eql` | AEAD tag compare on decrypt path | **Done** (`9937`) |
| Keccak `@memcpy` slice bounds | Every hash update on the metal path | **Done** (`9936` + `9935`) — `keccak_p` absorb/squeeze and `ShakeLike` buffered squeeze |
| Freestanding integration gate | `aurora/run.sh` stages prove RISC-V link + QEMU | **Open** — complements hosted `parity.rish`, does not replace it |
| CSR / MMIO / UART in `deciding`, `seed` | Boot relay, not `std` | **Aurora-owned** — TAME assertions in `.rye`, not strengthening passes |

**Rishi** stays on the hosted string/mem track (`trim`, `split`, `eql`, path builtins) — correct for the shell gate trio.

**Order when the main track reaches a natural pause:** (1) freestanding integration smoke (`aurora/run.sh` in CI), (2) optional `aurora-metal.rish` witness wrapper.

**Near — build (after main track holds green):**
- **Caravan capability table** — small Rye struct per child (`984` step 5).
- **Rye chronological version parser (accretion)** — `std.RyeVersion` (or `rye.version`) **beside** `SemanticVersion`, never replacing it: `parse`, `format`, and `order` for `YYYYMMDD.HHMMSS`. Fixed-width stamps already order by lexicographic compare; a parser earns its keep when the capability table or Tablecloth needs programmatic min-version bounds (`rye-versioning-style.md`, `173212`).

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
| **Our programs** | `.rye` | Rishi, seeds, Skate, witness tests — what we author |
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

**Reserved words** — high-value metaphors held until a surface earns them (`context/specs/reserved-vocabulary.md`). **`plot`** is reserved today; parity programs are **witnesses**.

**Parity contract (`145612`):**

- **Witnesses** — `.rye` programs in `rye/tests/` listed in `tools/parity.rish`; each one witnesses that baseline and strengthened `std` agree on behavior.
- **Compare:** baseline `vendor/zig-toolchain/lib` vs strengthened `rye/lib` — same test, same pinned Zig (`RYE_ZIG`).
- **Invoke:** `rye run rye/tests/<name>.rye` on both arms (`RYE_LIB` for baseline); exercises the real bridge path.
- **Hold:** exit code + stdout/stderr identical — assertions change what code *says*, never what it *does*.
- **Witnesses:** 69 programs, all GREEN (9934 mem split factories latest).

## The Through-Line

One value model, all the way down. The main work now is **Rye** growing surely, **Rishi** scripting the gates, and **strengthening** earning each `std` surface before the next layer composes. Garden memory in authored code flows through `init.garden`; inherited `ArenaAllocator` stays in std until `rye.garden` earns its keep. Tablecloth's ladder waits documented on the side.

---

*May the threads stay visible while they are open, and be tied off honestly when they close.*
