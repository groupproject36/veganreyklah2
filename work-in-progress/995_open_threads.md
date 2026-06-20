# 995 · Open Threads — The System Takes Shape

*A living snapshot of what has landed, what is closed, and what remains open. Updated after tonight's building session: Caravan bounded, Aurora deciding, the gate trio complete in Rishi, Wayland and editor research, the forge quarantined, and the whole-system map drawn.*

**Language:** EN
**Version:** `20260620.015312` (Rye chronological stamp)
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

- **Radiant sweep (014612).** `but` → `yet`/restructure across research, strengthening notes, and Mantra comments since the 054612 sweep (`0963662`).

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
- **`init.garden`** — TAME vocabulary in std.
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

**Near — study:**
- **Display-layer study** — Wayland protocol specs for Brushstroke. Ghostty (MIT) for Skate. River through public docs only (GPL-3.0).
- **Close reading** — packet format, commit rule, relay protocols from `gratitude/` before Comlink's format hardens.
- **TAME editor design** — Kakoune's select-then-act in Rye, Brix for settings, Rishi for behavior (`971`, `980`).
- **TAME editor — Zed architecture study** — Zed's core editor is GPL-3.0 (public design study only, same boundary as River); **GPUI** is Apache-2.0 and may inform GPU frame discipline. Study core/UI separation, multiplayer state model, and Tree-sitter-shaped syntax layers; implement as tame Rye on Brushstroke + Skate, extending `980` rather than shipping Rust.
- **JSON unified with Brix** — one value grammar for `.brix` brick records, serialized interchange, and Rishi literals; JSON as the wire face of Brix values rather than a parallel format. Grow from the plain key-value `.brix` descriptor already in Mantra.
- **Ink (markdown parser)** — tame Rye markdown for Mantra views, Forge pages, and docs surfaces. Survey permissive Zig parsers and mature Rust implementations (e.g. pulldown-cmark, MIT/Apache); clean-room Rye with TAME bounds on input size, nesting depth, and allocation per parse.
- **Comlink remoting** — value-based state sync over UDP, our own crypto, Pond enclosures (`971`).

**Horizon 2 milestones:**
- **Pond GUI** — Rishi REPL + Mantra in a Brushstroke window on x86_64 AMD.
- **The Forge** — Mantra-native forge, Brushstroke surface, Comlink replication, Pond CI (`982`).

**Horizon — inference & tensors** *(module names provisional; quarantine until designs earn them):*
- **Lantern** — local LLM inference (Ollama-shaped): pull and run models inside Pond enclosures, bounded memory in Tally gardens, value-based request/response API rather than a streaming pipe protocol.
- **Lattice** — tensor autograd (Tinygrad-shaped; **preferred** over heavier stacks): explicit buffers, smallest honest tensor surface, parity-gated numeric primitives before any model work.
- **Anvil** — training-framework scale (PyTorch/TensorFlow-shaped; far horizon): only after Lattice proves the numeric ground; study for discipline, implement in clean-room Rye if the need arrives.

**Ongoing — design:**
- **`pond.rish`** — the enclosure as a value; awaits Caravan isolation and Tally bounds.
- **The owner-key PKI** — rotation, revocation, and recovery.
- **The verify-flag hot path** — data-plane postconditions behind a `verify` flag.

## The Through-Line

One value model, all the way down. A Mantra line, a Brix brick, a Comlink message, a Pond policy, a Brushstroke frame — the same kind of thing: signed, named, bounded, owned. The sealed datagram between two harts is that line made real. The Pond GUI holds the same line at a higher level. Each new step tightens the line; each study tests it against how others built. We keep it simple, we keep it kind, and we grow the whole from the smallest part that already works.

---

*May the threads stay visible while they are open, and be tied off honestly when they close.*
