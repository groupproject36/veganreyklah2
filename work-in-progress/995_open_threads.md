# 995 · Open Threads — After Mantra Seed, the Garden Rename, and the sh→rish Question

*A fresh snapshot, taken after the four-pass strengthening frontier sealed, after Mantra's first seed planted, and after `init.arena` became `init.garden` across Rye's entire vocabulary. Names the new threads that opened tonight and carries forward the still-open ones.*

**Language:** EN
**Version:** `20260619.225712` (Rye chronological stamp)
**Last updated:** 2026-06-19
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Voice:** Reya 2

---

## What Just Landed

- **The crypto foundation, whole.** AEAD joined SHA3-512, Ed25519, and X25519 — every primitive parity-green, hosted and freestanding.
- **A sealed datagram across two harts.** `aurora/src/posted.rye`: hart 0 seals, hart 1 shape-casts and opens over a shared-memory mailbox.
- **`parity.rish` runs in our own shell.** The differential-parity gate in Rishi — proven GREEN and RED. The child keeps watch over the parent.
- **Rishi gained arithmetic and a real stdout.** `+`/`-`/`×`/`÷`, correct precedence, `say` on stdout.
- **Tally seed runs.** One `Region`, bump allocate, clear whole, 13 asserted invariants all green (`tally/seed.rye`).
- **Dual-editor setup committed.** `CLAUDE.md`, `.claude/rules/`, `tools/` examples; Zed and Claude Code share one project.
- **Design arc in four documents.** `977`, `978`, `985`, `986` — POSIX at the door, the living desktop stack, quarantined clean-room briefs. Ordered plan `10009`.
- **The strengthening frontier (9994–9991) sealed.** SHA3-256, mem diff primitives, `std.Io.Dir` boundary, `Dir.iterate` — all four through the gate, corpus grew 8 → 13, all green.
- **Mantra seed runs** (pass 9990). Weave, LCS diff, SHA3-256 store, `init / add / status`. Corpus at 14. The first living history in Rye.
- **`init.garden` replaces `init.arena`.** Rye's public API now uses TAME vocabulary throughout. `std.process.Init.garden` is the season allocator — allocate freely, clear on exit. The parity gate confirmed the rename is visible only in Rye's std (as intended): the weave test was updated to `page_allocator` so both stds produce identical output.
- **Rishi file I/O builtins.** `read-file`, `write-file`, `list-dir` — each behind the OS boundary. Round-trip test in `rishi/tests/file_io.rish`, all assertions green.
- **TAME Style spec + Claude rule.** `context/specs/tame-style.md` (root + Rye/Brix/Rishi supplements), `.claude/rules/tame-style.md`.
- **TAME assertion audit.** 12 highest-value assertions added to Rishi file I/O and Mantra commit chain. ~50 more in backlog.
- **Caravan microkernel brief (984).** Quarantined design: three kernel responsibilities, five invariants, path from seed to kernel.
- **s6, Nix, skalibs cloned into `gratitude/`.** SixOS and infuse already present. All thanked in `997_SYSTEM.md`.
- **External research: s6/SixOS/Nix/infuse (974).** What Caravan, Brix, and Tally inherit from each.
- **The Whole System brief (983).** Quarantined design composing every module — language, kernel, memory, store, shell, surface, network, enclosure — on its own ground.

## Threads Now Closed

- **The encrypted-datagram seed — tied off.** `posted.rye` runs; what remains is the real device.
- **Rishi reached `parity.rish` — tied off.** The gate runs in our own shell, GREEN and RED.
- **The network's name — tied off.** Comlink.
- **Tally seed — tied off.** One `Region`, 13 invariants, all green. Grows toward Tally v1.
- **Four strengthening passes (9994–9991) — tied off.** SHA3-256, mem diff, fs boundary, Dir.iterate. Corpus at 14, all green.
- **Mantra seed (9990) — tied off.** Weave, LCS diff, SHA3-256 store, `init / add / status`. First running history.
- **`init.arena` → `init.garden` — tied off.** TAME vocabulary in the public API; all callers updated.
- **`parity-selftest.rish` — tied off.** The gate proves RED in Rishi too. Uses `cp -r` and `sh -c` as temporary stand-ins until `list-dir` and `write-file` land.
- **Tally v1 — named gardens — tied off.** `tally/gardens.rye`: `Gardens`, three named regions, `add/get/clearOne/clearAll/totalRemaining`, 15/15 parity GREEN (`strengthening-compiler/9989`).
- **Brix minimum — tied off.** `.brix` at repo root: name, version, 9 tracked bricks. `mantra brix` prints; `mantra init` reads. Mantra knows the project. (Silo is now the store layer; Brix is the composing language.)
- **Mantra for the repo (seed) — tied off.** Commit-chain model, `mantra add` (no args) walks `.brix`, `mantra log` follows the chain. 9/9 bricks wove on first run. Multi-file manifest is the next growth pass.
- **Rishi file I/O builtins — tied off.** `read-file`, `write-file`, `list-dir` landed. Round-trip test in `rishi/tests/file_io.rish`, all green. Parity gate 15/15 GREEN.
- **Caravan seed — tied off.** One parent, one child, restart on fall. 3 planned failures, 3 restarts, child succeeds on the fourth spawn. 5 assertions confirmed GREEN (`caravan/seed.rye`).

## Threads Still Open

**Near — Horizon 1 threads:**
- **Device wire** — sealed datagram over emulated `virtio-net` between two QEMU machines; Comlink's next rung.

**Near — display layer:**
- **Display-layer study** — River (GPL-3.0) is studied through public Wayland protocol specs and documentation only, not cloned. Ghostty (MIT) may be cloned for close reading. Our terminal is **Skate**; our compositor surface is **Brushstroke**. Both written from scratch in Rye.
- **Brushstroke seed** — one native x86_64 window, one static frame, thin Wayland/Vulkan backend (`../active-designing/985`, `../active-designing/986`). Depends on River and Ghostty.

**Near — shell:**
- **`additive-gate.rish` — tied off.** Rishi orchestrates; awk classifies. The `.sh` fallbacks are removed — Rishi gates are the primary.
- **Rishi `lines` + `starts-with` — tied off.** String splitting and prefix checking. Paren depth fix across all parsers. 16/16 GREEN.

**Horizon 2 milestone:**
- **Pond GUI on x86_64 AMD** — Rishi REPL + live Mantra version control of `~/veganreyklah2` in a Brushstroke window (`../expanding-prompts/10009`).

**Ongoing — strengthen and grow:**
- **Continue the strengthening series** — the next `std` surfaces our tools lean on, each through the gate trio.
- **Caravan bounded — tied off.** Child runs inside a 256-byte Tally garden; exceeds budget → falls → supervisor restarts → child stays within bounds → 10 assertions GREEN (`caravan/bounded.rye`). Grows toward multi-child and chain-loading (`../active-designing/984`).
- **Close reading** — packet format, commit rule, relay protocols from `gratitude/` before Comlink's format hardens.
- **Aurora's deciding stage** — a relay stage that hands the next a value it chose.
- **Caravan kernel design** — decided: microkernel. Quarantined in `../active-designing/984`. Research in `../external-research/976`.
- **The Forge** — Mantra-native forge with Brushstroke surface, Comlink replication, Pond CI, key-based identity. Quarantined in `../active-designing/982`. Research in `../external-research/973`.
- **`pond.rish`** — the enclosure as a value; awaits Caravan isolation and Tally bounds.
- **The owner-key PKI** — rotation, revocation, and recovery.
- **The verify-flag hot path** — data-plane postconditions behind a `verify` flag (`../strengthening-compiler/9996`).

## The Through-Line

One value model, all the way down: a packet, a post, a Mantra line, a Brix brick, a Rye value — the same kind of thing, signed, named, bounded, owned. The sealed datagram between two harts is that line made real: a value, sealed and named, arriving on the far side as the same value it left as. The Pond GUI goal holds the same line at a higher level: a Rishi command, a Mantra weave, a Brushstroke pixel — still the same value, still bounded, still proven at every edge. Each new step tightens the line; each clone tests it against how others actually did it. We keep it simple, we keep it kind, and we grow the whole from the smallest part that already works.

---

*May the threads stay visible while they are open, and be tied off honestly when they close. May we read what we cloned closely, build what we imagined slowly, and keep the network — like the values it carries — small enough to love.*
