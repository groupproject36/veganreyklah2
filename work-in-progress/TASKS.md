# Tasks — The Granular Plan

**Language:** EN
**Last updated:** 2026-06-29 (open-threads archived; Skate next — Claude)
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Voice:** Reya 2
**Lens:** TAME — safety, performance, joy; SLC; Gall's Law

*This is the living, granular plan — the bench where the current rings are shaped. `ROADMAP.md` holds the why and the order; this file holds the what-now. It is **edited in place**: a task is checked when it lands, and the record of how it landed accretes in `../session-logs/`. Checked items are swept to a session log and pruned here when a section grows heavy. What is next lives here; what happened lives there.*

**Legend:** `[ ]` to do · `[~]` in flight · `[x]` done, pending sweep to a session log.

**Tracks:** **Rye OS** grows the system. **Linengrow** grows the first whole built on it. **Ground** is the shared discipline beneath both.

---

## Now — In Flight and Immediate

### Rye OS
- [x] **Run the witness suite on metal** — `rishi/bin/rishi run tools/parity.rish` green (116 `rye run` witnesses + four SLC-1); `parity-selftest.rish` green. Build with `HOME` on project disk (`/home/xy/veganreyklah2/.build-home`) — host tmpfs at `/home/xy` is full.
- [x] **SLC-1, Step 1 — the interactive loop** — `rishi repl` (bare `rishi` or `rishi repl`), in-process evaluator, bindings carried forward line to line; `:quit` / `:q`; witness `tools/slc1_repl_step1.rish` green.
  - [x] **1a — entry points** — bare `rishi` and `rishi repl` both start the loop; `rishi run` and `rishi version` unchanged.
  - [x] **1b — type** — fixed prompt `rishi> `; stdin via `takeDelimiterInclusive('\n')`; trim `\r\n` from each line.
  - [x] **1c — run** — `evalStatement` in-process; shared `Env`; evaluation errors print and continue (no exit).
  - [x] **1d — meta (minimal)** — `:quit` and `:q` end cleanly; other `:` lines report unknown meta-command.
  - [x] **1e — witness** — `tools/fixtures/slc1_repl_step1.input` + `tools/slc1_repl_step1.rish` assert binding carry-forward (`let x = 7` then `say "${x}"` → `7`).
  - [x] **1f — register** — `tools/slc1_repl_step1.rish` appended to `tools/parity.rish`.
- [x] **`init.garden` → `init.arena` harvest** — pristine `vendor/zig-toolchain` std uses `arena`; all authored `.rye` call sites migrated (`2026-06-29`). `brushstroke/wayland_seed.rye` link still needs Wayland dev headers on the host (unchanged).
- [x] **SLC-1 acceptance** — `tools/slc1_accept.rish` green; four verbs in one session; parity 120; gate trio confirmed on metal (`2026-06-29`). Closed on the **functional promise** — type, run, version, recall. Width migration on touched files and `width-check` refinement remain the **TAME-hardening milestone** (below), not folded into SLC-1.
- [x] **Cursor in ai-jail launcher** — `tools/cursor-jail.sh` + `tools/launch-cursor.rish` (tracked); `SOURCE.md` Step 6–9 and `enclosure-editors.md` updated; `squashfs-root/` and `.cursor-state/` gitignored; POSIX scaffold until Rishi script arguments graduate flag-handling (`2026-06-29`).

### Linengrow
- [x] **Infuse the vision** — place the business model and venture pitch in `linengrow/`, with a README connecting Linengrow to the Rye OS spine (this pass).
- [x] **Name SLC-L1** — record that the first Linengrow ring is the verifiable receipt (sign → append → receipt → verify), built from keypair + Mantra log + projection.

### Ground
- [x] **Grokipedia sweep** — Wikipedia links in our own markdown swapped where a comparable page exists; third-party clones left as-is.
- [x] **Merge the batch home** — when `design/foundations-and-kernel-horizon` settles, merge to `main` and push, so the living docs (ROADMAP, TASKS, Linengrow, foundations) reach the default tip.

---

## Next — After Now Lands

### Rye OS
- [x] **SLC-1, Step 2 — version** — session transcript + Mantra weave; scope [`active-designing/20260629-004912_slc-1-step-2-version.md`](../active-designing/20260629-004912_slc-1-step-2-version.md); Rishi drives Mantra as a separate seed (composition, not absorption).
  - [x] **2a — session buffer** — `History` ring of last 50 input lines (bounded, TAME).
  - [x] **2b — transcript** — in-memory `Transcript` records prompt, input, and caught errors (stdout horizon); flushed to `.mantra/session.log` on `:version`.
  - [x] **2c — `:history`** — print numbered entries from the session buffer.
  - [x] **2d — lazy init** — on first `:version`, ensure `.mantra/` exists (`mantra init` if needed).
  - [x] **2e — `:version`** — invoke `mantra add .mantra/session.log`; HEAD advances.
  - [x] **2f — witness** — `tools/slc1_version_step2.rish` green; registered in `parity.rish`.
- [x] **SLC-1, Step 3 — recall** — prior lines in-session; durable record is the weave from Step 2.
  - [x] **3a — `:recall <n>`** — `recallByIndex` + shared `runInputLine`; re-runs ring entry as if typed.
  - [x] **3b — `!<n>` alias** — shorthand via `recallByIndex` before the `:` meta block.
  - [x] **3c — witness** — `tools/slc1_recall_step3.rish` green; two `RE-RAN` prints prove re-run; registered in `parity.rish`.
- [x] **Rishi script arguments** — **RS-1** through **RS-3** under TAME hardening (all done).
- [x] **Launcher graduation** — **RS-3** under TAME hardening.

### TAME hardening — complete (`2026-06-29`)

Strengthening charter, seam-aware width, bare assert, script args, launcher graduation, and hosted width gate — **TH-0 through TH-7**, **RS-1 through RS-3**. Record: `session-logs/20260629-204910_th7-width-gate-yonder-convention.md` and prior TH/RS logs. Hosted `width-check` blocks in parity.

**Horizon and optional (still open):**

- [ ] **Aurora invariant notes (optional)** — say-why rationales beside `catch unreachable` in `aurora/src/seed.rye`; freestanding only; no width or assert lint.

- [ ] **Mantra CRDT weave (horizon)** — merge-always-succeeds-and-converges semantics from `external-research/yonder/20260617-195312_mantra.md`; SLC-1 seed uses LCS line weave only today.

- [ ] **TAME hygiene (as-you-touch)** — assertion-density backlog and `// invariant:` prefix in older code; address when each file is touched, not as a sweep.

- [ ] **Content-centric Rishi messenger (horizon)** — smallest IRC-meets-Dojo CLI over sealed, content-named datagrams; from `expanding-prompts/yonder/20260618-212012_content-centric-messaging.md`; Aurora/Comlink carry the networking seeds today.

- [ ] **Shape-casting for RISC-V bytecode (horizon)** — prove raw bytes match a declared type before trust; draw the shape-vs-execution seam plainly; from the same consumed prompt.

- [ ] **Ownerboot sovereignty (horizon)** — owner-key-sealed boot chain inverting trust at the reset vector; from `external-research/yonder/20260617-195612_ownerboot-riscv-caravan.md`; Caravan is live, the firmware path is horizon.

- [ ] **Unified identity and fractal address space (horizon)** — one seed deriving SSH, GPG, Sui, and Nostr keys; fractal address space shaped by Vedic whole-sign astrology (galaxy / star / planet); ties to Linengrow portable identity; from `expanding-prompts/yonder/20260618-215512_unified-keys-and-address-space.md`; Comlink carries the networking half today.

### Rye OS — further rings
- [ ] **Caravan capability table** — a small Rye struct naming what each child may do; the first true step toward the microkernel. Asserted; witnessed.
- [ ] **Skate text rendering** — text on screen; unlocks SLC-2.

### Linengrow
- [ ] **SLC-L1 scope note** — the hammock spec: the transaction fact, the keypair that signs it, the append to the log, the receipt as a pure fold, the verification. Draw the edge of complete; name what is out (settlement, the market).

### Ground
- [ ] **Kernel-direction memo** — graduate the microkernel leaning in `expanding-prompts/20260628-120912_*` into its own direction memo beside `20260628-043542`, when it feels fully settled. Same pattern as thin-frontend: deliberate, then record.
- [x] **Open-threads hygiene** — accreted `20260623-033012` snapshot archived to `work-in-progress/archive/`; redirect stub at old path; TASKS + ROADMAP are the live plan (`2026-06-29`).

---

## Soon — Medium Term

### Rye OS
- [ ] **SLC-2 — Pond GUI** — the Rishi+Mantra loop in a Brushstroke/Skate window on x86_64. Simple, lovable, complete at a small scope.
- [ ] **Comlink device wire** — a sealed datagram over virtio-net between two QEMU guests.
- [ ] **Comlink v1** — typed, content-named, sealed delivery between identities.
- [ ] **Brix v1** — a `.brix` course evaluating into a closure of content-addressed bricks in Tablecloth, per `active-designing/20260628-120912_brix-the-composer.md`.
- [ ] **Unified keys** — one owner seed deriving all keys.
- [ ] **Revitalization pass** — refresh the oldest active-designing briefs to the current direction, beginning with `active-designing/20260618-184912_recommended-architecture.md`; living docs in place, dated briefs superseded or stamped-with-provenance.

### Linengrow
- [ ] **SLC-L1 build** — verifiable receipts from keypair + Mantra log + projection. Witness: sign → append → receipt → verify, end to end.
- [ ] **SLC-L2** — a signed receipt delivered identity to identity over Comlink, sealed.

### Ground
- [ ] **Tablecloth v1** — the content-addressed store the package picture rests on.
- [ ] **TAME lints, AST tier** — begin only when a Zig parser is at hand or the need is proven: 70-line function limit ratcheted, bitwise/arithmetic precedence, defer-blank-line, dead declarations. Do not clone `tidy.zig` ahead of the need.

---

## Later — Horizons (decided in direction, grown by degrees)

### Rye OS
- [ ] **Caravan v1** — a supervision tree with a capability table; the microkernel taking shape from the hosted seed.
- [ ] **Pond v1** — Caravan isolation composed with Tally bounds, policy as a value.
- [ ] **The Forge** — Mantra served, Brushstroke drawn, Comlink replicated.
- [ ] **The TAME Editor**, **Comlink remoting** — select-then-act in Skate; value-based state sync over UDP.
- [ ] **Aurora toward verified boot** — the freestanding RISC-V seed grown toward a verified boot.
- [ ] **The kernel, built** — Caravan grown into a real microkernel on RISC-V (architecture decided; build last).
- [ ] **Language fork** — self-hosted compiler, Rye-native `std`, revisited from a mature whole if RISC-V-first genuinely demands it.
- [ ] **Inference stack** — Lantern, Lattice, Anvil, held furthest, after the living desktop composes.

### Linengrow
- [ ] **SLC-L3 — settlement** — a transaction settled on Sui with USDsui; the receipt verifiable on the ledger.
- [ ] **The platform horizons** — the computational data market, premium tiers, state-currency circulation, infrastructure licensing — grown from the business model in `../linengrow/`.
- [ ] **The civic horizons** — PBC formation, investor outreach, the first transparency campaign as proof of concept.

---

## Open Questions

- **Kernel direction** — is the microkernel leaning settled enough to graduate into a direction memo, or does it want more deliberation first?
- **Linengrow's home** — does Linengrow stay a folder in this repo, or graduate to its own repo (`xwb122m/linengrow-*`) once its first ring runs?
- **SLC-L1 and Sui** — confirm the first Linengrow ring uses pure foundations (keypair + log + projection) with no Sui, settlement deferred to SLC-L3. (Recommended: yes.)
- **Brix and Silo** — `infuse.nix` once seeded a "Silo" configuration language; Brix is now the composer. Is Silo retired into Brix, or a distinct config layer? Worth one clear line.
- **TASKS naming** — keep `TASKS.md`, or rename to the warmer `WORKBENCH.md`?

---

*May the next ring stay clear at the top of this list. May each task be small enough to finish and worth the finishing. May what we complete accrete as honest history, and what remains stay light in the hand.*
