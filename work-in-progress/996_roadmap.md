# 996 · The Roadmap — Growing the Whole from What Already Works

*A living plan for the work ahead, shaped by one law we hold close: a complex system that works grows from a simpler system that worked. So this roadmap never points straight at the finished, intricate whole. It lays out horizons — what runs now, what comes next, what composes from those, and the ambitious ends — and for each larger system it names the smaller working ones it is made of. We build by growing, and we ship something simple that runs at every step.*

**Language:** EN
**Version:** `20260620.203612` (Rye chronological stamp)
**Last updated:** 2026-06-20
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Voice:** Reya 2
**Lens:** TAME — safety, performance, the joy of the craft; and Gall's Law, that working wholes grow from working parts
**Status:** Living roadmap

---

## The Shape of This Plan

This plan draws its discipline from the active-designing stack: simplicity as single-stranded parts composed (`995`), the method of growing a language from proven ground (`996`), the gates that prove each step (`998`), the architecture the parts compose into (`997`), and the decision that Rye is its own language (`../context/specs/rye-as-its-own-language.md`). Above all it keeps Gall's Law: we reach for the smallest version that works, and let it become the larger one by degrees. No milestone here is built whole from scratch; each grows from the working systems beneath it.

---

## Horizon 0 — What Already Works (the ground we stand on)

These are the simple systems that run today. Everything ahead grows from them.

- **Rye runs, and is written in Rye** — a Zig-0.16 derivative with its own standard library and its own chronological versioning. The `rye` command (`run` and `build`) is itself a `.rye` program; Rye bootstraps once, then self-hosts its own build.
- **Aurora wakes on RISC-V, and grows stage by stage** — `rye build` emits a freestanding RISC-V binary that `qemu-system-riscv64` runs, through six living stages: a seed (a hart wakes, speaks one asserted line, halts), a three-stage relay (a boot as a flow of named values, each asserted), a content-named hart (SHA3-512 on bare metal), a whole sealed message (X25519 + AEAD + SHA3 + Ed25519, sealed and opened freestanding), and — across two harts — the wire (a shared-memory mailbox) and a posted datagram.
- **A sealed datagram crosses between two harts** — Alice seals on hart 0; Bob, on hart 1, reads the raw bytes off a shared-memory wire, shape-casts them, verifies the attestation, confirms the content-name, derives the shared secret from his own key, and opens it. The content-name matches the hosted test byte-for-byte: the move that turns the whole networking arc into something that runs, running.
- **The strengthening series is live** — SHA3-512, the Keccak sponge beneath it, and the everyday `std` our own tools lean on (`mem.trim`, `mem.eql`, `mem.findScalar`, `fmt.parseInt`), each given stated invariants and each parity-green, recorded in the strengthening-compiler stack.
- **The crypto foundation is proven, primitive by primitive** — the content hash (SHA3-512, strengthened), signing (Ed25519), key agreement (X25519), and the authenticated seal (AEAD: ChaCha20-Poly1305) all run in Rye's own std, hosted and freestanding alike, and stand parity-green: the foundation the network and identity rest on (`../strengthening-compiler/9995`).
- **The gate trio runs** — `parity.rish` (behavior), `parity-selftest.rish` (proves RED on divergence), `additive-gate.rish` (shape). All three run in Rishi; sixty-five witnesses, all green.
- **Rishi runs** — a shell interpreter in Rye with comments; `let` of strings, integers, booleans, lists, and records; string interpolation that composes a value into text (`"${a}/${b}"`); `say`; `==`/`!=` comparison; list membership with `contains`; field access with `record.field`; running a command with `run` (its result a record of `out`, `err`, `code`, `ok`); transforming and filtering lists with `map` and `where`; and `assert` as a gate that exits non-zero with its reason. Built by `rye build`.
- **Rishi gained arithmetic and a real stdout** — integer `+`/`-`/`×`/`÷` with correct operator precedence via two-layer recursive descent, parenthesized grouping, and `say` rebound from stderr to stdout. Nine arithmetic assertions in `rishi/tests/arithmetic.rish`, all green. The shell can now compute, compose, and speak.
- **The parity gate runs in Rishi** — `tools/parity.rish` runs each witness `.rye` through `rye run` (baseline via `RYE_LIB=vendor/zig-toolchain/lib`, strengthened via default `rye/lib`), compares outputs as one value, and asserts the verdict. Proven GREEN across 65 programs and RED on tamper (`parity-selftest.rish`).
- **The strengthening frontier (9994–9991) is sealed** — SHA3-256 (content-naming primitive), mem diff primitives (`copyForwards`, `startsWith`, `endsWith`, `find`, `splitScalar`), `std.Io.Dir` filesystem boundary assertions, and `Dir.iterate` name invariants and exhaustion state — all four through the gate, 14 witnesses, all green.
- **Mantra seed runs** — the smallest version-control that runs: a Weave holds the full history of a text file as Lines with stable positions and generation-parity presence; `computeDiff` finds the minimal LCS edit; the store content-names every weave state by its SHA3-256 digest. `mantra init / add / status` confirmed end-to-end. Pure LCS test becomes a witness (`../strengthening-compiler/9990`).
- **`init.garden` replaces `init.arena` in Rye's vocabulary** — `std.process.Init.garden` is Rye's name for the season allocator: allocate freely within the session, clear whole on exit. The TAME vocabulary (`garden`) now lives in the public API; `arena` recedes to an implementation detail inside `start.zig`. Rishi, Rye, Mantra, and all benchmark callers updated.
- **Seeds defined in `976`.** Every module grows from the smallest version that runs; the catalog and planting discipline live in `active-designing/976_what_we_mean_by_seed.md`.
- **Seven hosted/freestanding seeds in one arc** — Caravan (seed → chain), Brushstroke (stdout + Wayland), Comlink (posted + hosted wire), Aurora deciding — code advancing; design (~20 active-designing docs) now leads until build catches up (`10017`).
- **Comlink hosted wire** — sealed datagram over localhost UDP (`comlink/hosted_wire.rye`); virtio-net is next (`10016`).
- **Rishi string builtins** — `length`, `trim`, `slice`, `lines`, `starts-with`, `ends-with`, `split`, `join`, `contains`, infix `index-of`; gate trio 65/65 GREEN.
- **Skate text grid** — monospace 8×8 glyphs on Brushstroke Wayland seed; headless selftest green (`10023` Track A).
- **Strengthening passes 9979–9938** — `trimStart` … `mem.endsWith`. Each through the gate; witness count 17 → 65.
- **Garden memory policy** — authored `.rye` uses `init.garden.allocator()`, never `ArenaAllocator`; no std `GardenAllocator` rename; owned wrapper at `rye.garden` / `tally/heap-garden.rye` when built (`inherited-names.md`, TAME rules).

---

## Horizon 1 — Short-Term (the next simple systems, each small and proven)

Each is a thing that runs on its own, added by degrees, behind the gates.

- [ ] **The wire as a real device** — carry a sealed datagram over an emulated `virtio-net` between two QEMU machines, growing the two-hart shared-memory wire (done, Horizon 0) into a true network link. A device driver and two communicating instances: the meatier climb where Comlink fully begins.
- [x] **Caravan seed** — one parent, one child, restart on fall (`caravan/seed.rye`). Grows through bounded and twin toward Caravan v1.
- [x] **Caravan bounded** — supervision + Tally garden composed (`caravan/bounded.rye`).
- [x] **Caravan twin** — two children, separate gardens (`caravan/twin.rye`).
- [x] **Caravan chain** — ordered startup wake → prove; per-stage restart (`caravan/chain.rye`; `984` step 4).
- [x] **Tally seed — one region, asserted edges** — one bounded `Region` struct over a caller-provided backing slice; bump allocate within stated edges, fail past the boundary, clear whole in one gesture. 13 hosted `debug.assert` calls, all green (`tally/seed.rye`). Grows toward Tally v1.
- [ ] **Close reading of cloned sources** — packet format, commit rule, relay protocols from what we vendored in `gratitude/`, with actionable notes for Comlink before the wire format hardens (`995`, `10007`).
- [x] **Aurora's deciding stage** — four stages: wake, prove, decide, rest. The deciding stage reads ISA extensions, chooses a configuration path, tags the choice. Clean exit on QEMU virt (`aurora/src/deciding.rye`).
- [x] **Grew Rishi to `parity.rish`** — shipped one proven feature at a time: `==`/`!=`, `assert`, lists, `contains`, records with field access, `run`, `map`/`where`, and string interpolation — and then the gate itself (Horizon 2 below, reached early). `tools/parity.rish` runs GREEN, and RED on a real divergence.
- [x] **Strengthening passes 9994–9991** — SHA3-256 (9994), mem diff primitives (9993), `std.Io.Dir` boundary assertions (9992), `Dir.iterate` (9991). All four through the gate, 14 witnesses, all green.
- [x] **Mantra seed** — Weave, LCS diff, SHA3-256 store, `init / add / status`. Runs end-to-end; pure LCS test among witnesses (`../strengthening-compiler/9990`).
- [x] **Tally v1 — named gardens** — `tally/gardens.rye`: `Gardens` struct holding named `Region` values, `add/get/clearOne/clearAll/totalRemaining`. Three named gardens for the stack: `blob`, `diff`, `frame`. Corpus grows to 15/15 GREEN (`../strengthening-compiler/9989`).
- [x] **Mantra for `~/veganreyklah2` (seed)** — commit-chain model, `mantra add` (no args) walks `.brix`, `mantra log` follows the HEAD chain. 9/9 bricks wove. Multi-file manifest (separate weave per file) is the next growth pass.
- [ ] **Display-layer study** — River studied through public Wayland specs only (GPL-3.0, not cloned). Ghostty (MIT) may be cloned. Our terminal is **Skate**; our surface is **Brushstroke**. Both from scratch in Rye.
- [x] **Rishi file I/O builtins** — `read-file`, `write-file`, `list-dir` behind OS-boundary wrappers. Round-trip test in `rishi/tests/file_io.rish`, all assertions green. Parity gate 15/15 GREEN.
- [x] **`additive-gate.rish`** — Rishi orchestrates (`git diff` + awk classifier). The `.sh` fallbacks are removed. Gate trio complete in Rishi.
- [x] **Brushstroke hosted seed** — Frame value, stdout redraw (`brushstroke/seed.rye`; `10011`).
- [x] **Brushstroke Wayland seed** — one native window, Frame → SHM buffer (`brushstroke/wayland_seed.rye`; `10012`).
- [x] **Comlink hosted wire** — sealed datagram over localhost UDP (`comlink/hosted_wire.rye`; `10014` Track D).
- [x] **Rishi string builtins** — `length`, `trim`, `slice`, `lines`, `starts-with`, `ends-with`, `split`, `join`, `contains`, infix `index-of` (`10023` Track C).
- [x] **Skate text grid** — monospace glyph rendering on the Wayland seed (`skate_grid.rye`, `font8x8_data.rye`, `wayland_seed.rye`; `10023` Track A).
- [x] **Strengthening 9979–9938** — everyday `std` surfaces through the gate (`trimStart` … `mem.endsWith`; see `strengthening-compiler/9938`–`9987`).
- [ ] **Device wire (virtio-net)** — two QEMU guests (`10016`).
- [ ] **Rye chronological version parser** — accrete `std.RyeVersion` beside `SemanticVersion` (`parse` / `format` / `order` for `YYYYMMDD.HHMMSS`); unblocks Caravan capability min-version and Tablecloth policy (`rye-versioning-style.md`, `995`).
- [ ] **Continue the strengthening series** — the next `std` surfaces our tools depend on, each through the gate trio, each recorded in the strengthening-compiler stack.

---

## Horizon 2 — Medium-Term (compose the simples into larger working systems)

Each milestone here is *made of* the working systems above.

- [x] **`parity.rish` runs** — made of: Rishi (lists, records, `run`, `map`/`where`, interpolation, `assert`) + the parity logic. The gate, rewritten in our own shell — proven GREEN, and RED on a real divergence (`../tools/parity.rish`).
- [ ] **Comlink v1 — the network module** *(see `../external-research/981`)* — made of: the encrypted-datagram seed grown into typed, content-named, sealed message delivery, exactly-once by hash, carrying values between identities.
- [ ] **Unified keys v1** — made of: one owner seed deriving the keys a person needs (ed25519 for SSH/GPG/Sui, secp256k1 for Nostr), separated for safety and recovered as one (`../external-research/981`).
- [ ] **Brix v1** — made of: a lawful composition combinator over brick descriptors, backed by Tablecloth (the content-addressed store). Describes a simple system reproducibly.
- [ ] **Tablecloth v1** — made of: a general-purpose content-addressed store grown from Mantra's `.mantra/blobs/` into a full, independently queryable artifact store (`expanding-prompts/10022_tablecloth_v1_seed.md`, ladder from `10018`).
- [ ] **Tally v1** — made of: the process-garden pattern Rye already uses, grown into a named, bounded region allocator with asserted edges.
- [ ] **Caravan v1** — made of: the simplest working supervision (one parent that never dies, one child, restart on fall), grown toward a small tree and chain-loaded startup.
- [ ] **Pond v1** — made of: Caravan v1's isolation **composed with** Tally v1's bounds — one allow-listed path, one resource bound, opened from a policy that is a value (`pond.rish`).
- [ ] **Mantra for `~/veganreyklah2`** — made of: Mantra seed grown into multi-file weave tracking the full repository; content-named HEAD chain, `mantra log`, integration tested in a Rishi script.
- [x] **Brix minimum** — `.brix` at the repo root: `name`, `version`, and `file` entries for the 9 tracked bricks. Mantra reads it at startup — `mantra brix` prints the descriptor; `mantra init` reports the project name and file count. The first course toward Brix v1.
- [ ] **Pond GUI — Rishi REPL + Mantra in a Brushstroke window** — made of: Brushstroke seed + Mantra seed + Rishi file I/O, composing into a single native x86_64 window with a Rishi text area and live Mantra version control of the repository (`../expanding-prompts/10009`, `../active-designing/986`).

---

## Horizon 3 — Ambitious Milestones (the complex wholes, each grown from the working parts)

The far ends. Each is named with the simpler working systems it is composed of, so the path to it is always a growing, never a leap.

- [ ] **Rye, a genuinely separate language** — made of: the strengthened `std` + a growing divergence in syntax and semantics, including borrow-checking-style guarantees over Tally's gardens (`../external-research/983`), compiling to RISC-V as a first-class target. Grown from the Zig-derivative, never rewritten from scratch.
- [ ] **The full family, composing through one value model** — made of: Rye + Brix + Tablecloth + Rishi + Mantra + Comlink, each grown from its v1, sharing one value model so values flow seam-free from a keystroke to the wire.
- [ ] **The content-centric messenger** — made of: Comlink + Mantra + unified keys + Rishi's `talk` — an IRC-meets-Dojo where a message is a named, sealed value carried home (`../external-research/982`).
- [ ] **The devotional social layer** — made of: the messenger + Nostr-simple store-and-forward relays on our coherent core, curated by honest structure, true to the values (`../external-research/984`).
- [ ] **The fractal address space** — made of: unified keys + a derivation tree shaped as galaxies, stars, and planets (d5 × d12 = d60), with admins who coordinate and never command (`../external-research/981`).
- [ ] **Aurora — the boot on RISC-V** — made of: the seed and relay, grown stage by stage into a verified, named-value boot from an immutable root.
- [ ] **Pond — a trustworthy daily enclosure** — made of: Pond v1, hardened pass by pass over Caravan's isolation and Tally's gardens, until it is the room our agents work inside.
- [ ] **Brushstroke, web-portable** — made of: Brushstroke seed grown with a `wasm32-freestanding` backend, so any Pond application runs in a browser surface without rewriting. The same frame-garden discipline, the same widget seam, a different surface below.
- [ ] **A self-hosted, RISC-V-cohesive Rye system** — made of: Aurora (boot) + Caravan (kernel) + Tally (memory) + Brix (composition) + Tablecloth (store) + Mantra (memory of the system) + Comlink (the network) + Rishi (the hand) + Pond (the enclosure) — the whole machine, grown from every working part beneath it, belonging wholly to the one who runs it.

---

## The Discipline This Plan Obeys

- **Ship something simple that runs at every step.** A thing that runs, however humble, teaches more than a grand design that does not.
- **Grow; never design the whole from scratch.** Each milestone evolves from the working system before it. When something cannot be grown, we begin again from a simpler thing that works, rather than patching a thing that never lived.
- **Prove each step through the gates.** Behavior preserved, shape additive, divergence caught — green before we compose the next layer.
- **Keep it loose and single-stranded.** Each part about one thing, composed side by side, so any one can be grown or replaced without unweaving the rest.
- **Stay in close touch with what each system is truly for.** We measure by whether the thing actually works for its purpose, not by how finished it looks.

---

## Where We Are Now — Build Catches Design

**Ratio going forward:** two-thirds implementation, one-third design (`10017`). Tablecloth store prose is unified in `10018`–`10022`; **v1 code deferred** until Rye, Rishi, and strengthening hold the main track.

**Highest-leverage build threads (ordered):**

1. **Strengthening series** — next `std` surface through the gate trio (`9937` and below; `998`)
2. **Rishi** — builtins as gates and Pond policy need them (core string/path set landed)
3. **Comlink virtio-net** — device wire between QEMU guests (`10016`, `993`)
4. **Caravan capability table** — `984` step 5 (pairs with **RyeVersion** accretion when min-version bounds are needed)
5. **Tablecloth v1** — after 1–2 stay green (`10022`; Mantra blobs → queryable store)

**Aurora metal lane** (`200312`, detail in `995`): freestanding stages ride strengthened **crypto**, **`mem.eql`**, and the **prefix/suffix pair** (`9938`–`9939`). RISC-V uses the scalar `eql` path. **Next on metal** when the main track pauses: **`crypto.timing_safe`**, Keccak **`@memcpy`** slice bounds, then freestanding **integration smoke** (`aurora/run.sh` in CI — complements hosted `parity.rish`, does not replace it).

The Pond GUI (`10009`, `986`) composes when Brushstroke + Skate + Mantra + Rishi meet on x86_64. Aurora's RISC-V arc continues in parallel.

### What to Build Next, and Why

Tally v1 gardens, Brix minimum, Mantra repo chain, Rishi gate trio, Caravan chain, Brushstroke Wayland, Comlink hosted wire, Skate glyph grid, path naming family, garden-memory policy, **SemanticVersion** trio, **mem** compare/copy/sentinel arc, **timing_safe.eql (9937)** on the metal path, mem iterators through **WindowIterator (9954)**, mem.join (9961), cut family (9958–9960) — all done. **Strengthening the next `std` surface (9936)** stays the honest next step on the main track; **Keccak `@memcpy`** and freestanding smoke remain on the Aurora metal lane; **RyeVersion** accretion waits beside the capability table.

---

## The Steps Just Taken

Strengthening through **9938**, Aurora metal lane documented (`200312`), garden-memory policy in TAME and rules, Rishi builtins and parser fix, Skate grid, parity via `rye run`, witnesses vocabulary, style audit shipped.

**Strengthening passes 9979–9938** (`143312`–`201912`): `trimStart` … `mem.endsWith`. Witness count 17 → 65, all green.

**Version parser thread (`173212`–`174312`)** — documented in `995` Near build: accrete `std.RyeVersion` beside `SemanticVersion` when capability table or Tablecloth needs programmatic bounds; lexicographic compare on fixed-width stamps suffices until then.

**Garden memory (`161112`)** — authored code: `init.garden` only; no `ArenaAllocator`; no std `GardenAllocator`; owned wrapper horizon at `rye.garden` / `tally/heap-garden.rye`. TAME + Cursor + Claude rules.

**Rishi** (`151212`–`153812`): `split`, `join`, `ends-with`, `contains`, infix `index-of`; parser reorder + `isWordHyphen`.

**Skate** (`050912`+): `.rye` grid modules, Wayland monospace render, headless selftest.

**Parity** (`145612`): witnesses run through `rye run`; recursive `.rye` bridge in `rye/src/main.rye`.

**Garden vocabulary (phase 2)** — locals and authored code say `garden`; `ArenaAllocator` inherited; audit GREEN (`994_style_audit.md`, `155212`).

**Earlier arc (9994–9989):** SHA3-256, mem diff, `std.Io.Dir`, `Dir.iterate`, Mantra seed, Tally v1 gardens, Brix minimum, `init.garden` phase 1.

---

*May we grow the whole from what already works, and trust each small running thing as it carries the next. May every horizon arrive by degrees, never by a leap. And may the system we are building stay simple enough, at every stage, to be loved, understood, and grown a little further tomorrow.*
