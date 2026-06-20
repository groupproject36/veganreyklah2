# 995 · Open Threads — The System Takes Shape

*A living snapshot of what has landed, what is closed, and what remains open. Updated after tonight's building session: Caravan bounded, Aurora deciding, the gate trio complete in Rishi, Wayland and editor research, the forge quarantined, and the whole-system map drawn.*

**Language:** EN
**Version:** `20260620.020712` (Rye chronological stamp)
**Last updated:** 2026-06-20
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Voice:** Reya 2

---

## What Just Landed (this session)

- **Caravan bounded.** Supervision + Tally garden composed. Child exceeds 256-byte budget → falls → supervisor restarts → child stays within bounds. 10 assertions GREEN (`caravan/bounded.rye`).
- **Aurora deciding stage.** Four stages: wake, prove, decide, rest. The boot reads ISA extensions and chooses a configuration path. Clean exit on QEMU RISC-V (`aurora/src/deciding.rye`).
- **Gate trio complete in Rishi.** `parity.rish` (behavior), `additive-gate.rish` (shape). The `.sh` fallbacks are removed.
- **Rishi `lines` + `starts-with`.** String splitting and prefix checking. Paren depth fix across all parsers. 16/16 GREEN.
- **The Whole System (983).** Every module composed — language, kernel, memory, store, shell, surface, network, enclosure.
- **The Forge (982).** Quarantined: four layers (Mantra, Brushstroke, Comlink, Pond), key-based identity, group projects.
- **Caravan microkernel (984).** Quarantined: three kernel responsibilities, five invariants.
- **s6/Nix/infuse research (974).** What Caravan, Brix, Tally inherit.
- **Wayland/compositor research (972).** River's separated architecture, Omarchy's keybindings, TAME desktop mapping.
- **Editors/remoting research (971).** Kakoune's select-then-act, Brix for settings, Comlink remoting.
- **Manyana honored in SYSTEM.md.** CRDT weave ancestor of Mantra.
- **Multi-license strategy.** MIT + Apache 2.0 for code; CC-BY-4.0 for docs.
- **GPL compliance statement.** Gitlinks only; River studied through public specs; clean-room boundary.
- **Strengthening pass 9988.** `allocPrint` + `trimEnd`, corpus 16/16 GREEN.
- **TAME assertion audit.** 12 fixes in Rishi + Mantra.
- **TAME Style spec + Claude rule.** Root + Rye/Brix/Rishi supplements.
- **Skate named.** Our terminal — GPU-accelerated text in a Brushstroke window.

- **Formats, editors, inference research (`970`).** JSON/Brix unification, Scribble markdown survey, Zed/GPUI study, Ollama/Tinygrad/PyTorch/TensorFlow boundaries.
- **Horizon modules quarantined (`978`).** Scribble, Lantern, Lattice, Anvil on one value grammar; editor extends `980`.

## Threads Now Closed

- **Crypto foundation** — AEAD, SHA3-512, Ed25519, X25519. Parity-green, hosted and freestanding.
- **Sealed datagram** — `posted.rye`: two harts, shared-memory mailbox.
- **`parity.rish`** — the gate in our own shell, GREEN and RED.
- **Rishi arithmetic + stdout** — `+`/`-`/`*`/`/`, correct precedence, `say`.
- **Tally seed** — one Region, 13 invariants.
- **Tally v1 named gardens** — `Gardens`, blob/diff/frame, 15/15 GREEN.
- **Strengthening 9994–9988** — SHA3-256, mem diff, fs boundary, Dir.iterate, allocPrint/trimEnd. Corpus 16.
- **Mantra seed** — weave, LCS diff, SHA3-256 store, init/add/status.
- **Mantra for the repo (seed)** — commit chain, add-all walks `.brix`, log follows chain. 9/9 bricks.
- **`init.garden` (phase 1)** — `std.process.Init.garden` renamed from upstream `arena`; benchmarks and callers use `init.garden.allocator()`. Local variables, docs, and heap-level names remain (`session-logs/99970`).
- **Brix minimum** — `.brix` descriptor, 10 tracked bricks.
- **Rishi file I/O** — `read-file`, `write-file`, `list-dir`.
- **Rishi `lines` + `starts-with`** — string splitting, prefix checking, paren depth fix.
- **Caravan seed** — parent/child restart, 5 assertions.
- **Caravan bounded** — supervision + Tally garden, 10 assertions.
- **Aurora deciding stage** — wake, prove, decide, rest.
- **`additive-gate.rish`** — gate trio complete in Rishi. `.sh` fallbacks removed.
- **`parity-selftest.rish`** — the gate proves RED.
- **Brix rename (Silo → Brix)** — composing language vs store layer.
- **TAME Style spec** — `context/specs/tame-style.md` + Claude rule.
- **GPL compliance** — gitlinks, River not cloned, clean-room boundary.

## Threads Still Open

**Near — build:**
- **Brushstroke seed** — one native x86_64 window, one static frame. Written from scratch in Rye, informed by public Wayland specs (`985`, `986`, `988`). The display layer is the next frontier.
- **Device wire** — sealed datagram over emulated `virtio-net` between two QEMU machines; Comlink's next rung.
- **Caravan multi-child** — grow the bounded seed toward two children with separate gardens, then chain-loading (`984`).

**Near — strengthen:**
- **Continue the strengthening series** — the next `std` surfaces our tools lean on, each through the parity gate. Corpus at 16.
- **TAME assertion backlog** — ~50 locations identified in the audit, not yet fixed. Addressed as code is touched.

**Near — vocabulary (`arena` → `garden`):**
- **Finish the garden vocabulary sweep** — Tally's metaphor should read consistently in our code and prose. Phase 1 landed `init.garden` on `std.process.Init`; the rest is still open.
  - **Local names in our programs** — `const arena = init.garden.allocator()` → `garden` in `rye/src/main.rye`, `rishi/src/main.rye`, and the three `std` benchmark entrypoints (`Random`, `hash`, `crypto`). Function parameters that mean season memory (`resolveRyeLib`, etc.) follow suit.
  - **Comments and bridges** — update comments that still say "process arena" where the API is now `init.garden` (`rye/src/main.rye`).
  - **Learning and reference docs** — `rye/README.md`, `rye-learning-process/998_ALMANAC.md` still cite `init.arena`; align to `init.garden` and keep the bridge sentence (*garden cleared whole on exit*).
  - **`context/specs/inherited-names.md`** — reconcile with phase 1: `Init.garden` is an approved Rye public field; **`ArenaAllocator`** and `std.heap.ArenaAllocator` stay inherited Zig names.
  - **`rye/lib/std/start.zig`** — internal `arena_allocator` / `arena_backing_allocator` locals could become `garden_allocator` where we own the file (parity gate after).
  - **Strengthening notes** — `9989_tally_gardens.md` future `tally/arena.rye` → name `tally/heap-garden.rye` or fold into `gardens.rye`.
  - **External-research pedagogy** — `994` may keep *arena* when citing Urbit's loom or CS literature as the generic term; our prose there already maps *arena → garden Tally*. No blind sed in gratitude or unmodified upstream std.
  - **TAME Style example** — `996_TAME_STYLE.md` `arena: Allocator` example could add `garden: Allocator` beside it.
  - **Out of scope** — `std.heap.ArenaAllocator`, thousands of inherited `arena` locals inside unmodified `rye/lib/std/**`; those remain Zig vocabulary until a deliberate std fork pass.

**Near — study:**
- **Display-layer study** — Wayland protocol specs for Brushstroke. Ghostty (MIT) for Skate. River through public docs only (GPL-3.0).
- **Close reading** — packet format, commit rule, relay protocols from `gratitude/` before Comlink's format hardens.
- **TAME editor design** — Kakoune's select-then-act in Rye, Brix for settings, Rishi for behavior (`971`, `980`, `978`).
- **TAME editor — Zed architecture study** — GPU frame discipline from permissive GPUI patterns; GPL core study-only (`970`). Implements on Brushstroke + Skate.
- **JSON unified with Brix** — one value grammar (`970`, `978`); grow from `.brix` descriptor in Mantra.
- **Scribble (markdown parser)** — tame Rye CommonMark subset (`970` survey, `978` design); Zmd, pulldown-cmark close-reading targets.
- **Comlink remoting** — value-based state sync over UDP, our own crypto, Pond enclosures (`971`).

**Horizon 2 milestones:**
- **Pond GUI** — Rishi REPL + Mantra in a Brushstroke window on x86_64 AMD.
- **The Forge** — Mantra-native forge, Brushstroke surface, Comlink replication, Pond CI (`982`).

**Horizon — inference & tensors** *(see `978`):*
- **Lantern** — local LLM inference (Ollama-shaped; MIT study in `970`): Pond-enclosed, value-based API.
- **Lattice** — tensor autograd (Tinygrad-shaped; **build first**): parity-gated primitives in Tally gardens.
- **Anvil** — training-framework scale (PyTorch/TensorFlow-shaped; far horizon): reserved name until Lattice proves numeric ground.

**Ongoing — design:**
- **`pond.rish`** — the enclosure as a value; awaits Caravan isolation and Tally bounds.
- **The owner-key PKI** — rotation, revocation, and recovery.
- **The verify-flag hot path** — data-plane postconditions behind a `verify` flag.

## The Through-Line

One value model, all the way down. A Mantra line, a Brix brick, a Comlink message, a Pond policy, a Brushstroke frame — the same kind of thing: signed, named, bounded, owned. The sealed datagram between two harts is that line made real. The Pond GUI holds the same line at a higher level. Each new step tightens the line; each study tests it against how others built. We keep it simple, we keep it kind, and we grow the whole from the smallest part that already works.

---

*May the threads stay visible while they are open, and be tied off honestly when they close.*
