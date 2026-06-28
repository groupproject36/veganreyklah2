# Tasks — The Granular Plan

**Language:** EN
**Last updated:** 2026-06-28
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Voice:** Reya 2
**Lens:** TAME — safety, performance, joy; SLC; Gall's Law

*This is the living, granular plan — the bench where the current rings are shaped. `ROADMAP.md` holds the why and the order; this file holds the what-now. It is **edited in place**: a task is checked when it lands, and the record of how it landed accretes in `../session-logs/`. Checked items are swept to a session log and pruned here when a section grows heavy. What is next lives here; what happened lives there.*

**Legend:** `[ ]` to do · `[~]` in flight · `[x]` done, pending sweep to a session log.

**Tracks:** **Rye OS** grows the system. **Linengrow** grows the first whole built on it. **Ground** is the shared discipline beneath both.

---

## Now — In Flight and Immediate

### Rye OS
- [ ] **Run the witness suite on metal** — build `rye`, run `rishi/bin/rishi run tools/parity.rish` once; seal the thin-frontend arc green. If any of the 17 re-forked files surface an old postcondition, meet it at the call site per `work-in-progress/20260628-044200_call-site-harvest.md` — never by copying `std` back.
- [ ] **SLC-1, Step 1 — the interactive loop** — add `rishi repl` (bare `rishi` or `rishi repl`), reusing the existing evaluator, carrying the binding environment forward line to line. Leave `rishi run <file>` and `rishi version` untouched. Witness: two lines where the second depends on a `let` from the first.
- [ ] **Width migration Phase 1b — `mantra/*`** — migrate authored widths to `u32`/`u64` per the supplement; `width-check.rish` green. Decoupled from any fork.

### Linengrow
- [x] **Infuse the vision** — place the business model and venture pitch in `linengrow/`, with a README connecting Linengrow to the Rye OS spine (this pass).
- [x] **Name SLC-L1** — record that the first Linengrow ring is the verifiable receipt (sign → append → receipt → verify), built from keypair + Mantra log + projection.

### Ground
- [x] **Grokipedia sweep** — Wikipedia links in our own markdown swapped where a comparable page exists; third-party clones left as-is.
- [x] **Merge the batch home** — when `design/foundations-and-kernel-horizon` settles, merge to `main` and push, so the living docs (ROADMAP, TASKS, Linengrow, foundations) reach the default tip.

---

## Next — After Now Lands

### Rye OS
- [ ] **SLC-1, Step 2 — `version`** — a verb that writes the session transcript into Mantra and advances HEAD; Rishi drives Mantra as a separate seed (composition, not absorption). Witness: a blob and HEAD advance after `version`.
- [ ] **SLC-1, Step 3 — `recall`** — prior lines in-session, and the last saved transcript read back from Mantra's HEAD on a fresh start. Witness: a prior line returns; a saved session reads back.
- [ ] **SLC-1 acceptance** — type → run → version → recall closes on metal; gate trio green; pristine-`std` guard green; `rishi run`/`version` behavior unchanged.
- [ ] **Caravan capability table** — a small Rye struct naming what each child may do; the first true step toward the microkernel. Asserted; witnessed.
- [ ] **First TAME lints (Phase C)** — grow `tools/tame-check.rish` beside the `mantra/*` work, cheapest first, each with a witness: unqualified-assert (flag `std.debug.assert(` / `debug.assert(`), no `Self = @This()`, no tabs / trailing whitespace.
- [ ] **Skate text rendering** — text on screen; unlocks SLC-2.

### Linengrow
- [ ] **SLC-L1 scope note** — the hammock spec: the transaction fact, the keypair that signs it, the append to the log, the receipt as a pure fold, the verification. Draw the edge of complete; name what is out (settlement, the market).

### Ground
- [ ] **Kernel-direction memo** — graduate the microkernel leaning in `expanding-prompts/20260628-120912_*` into its own direction memo beside `20260628-043542`, when it feels fully settled. Same pattern as thin-frontend: deliberate, then record.
- [ ] **Open-threads hygiene** — archive the accreted "What Just Landed" stack in `20260623-033012_open-threads.md` into `../session-logs/` (history's true home); let TASKS hold open questions going forward.

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
- **SLC-L1 and Sui** — confirm the first Linengrow ring uses pure primitives (keypair + log + projection) with no Sui, settlement deferred to SLC-L3. (Recommended: yes.)
- **Brix and Silo** — `infuse.nix` once seeded a "Silo" configuration language; Brix is now the composer. Is Silo retired into Brix, or a distinct config layer? Worth one clear line.
- **TASKS naming** — keep `TASKS.md`, or rename to the warmer `WORKBENCH.md`?

---

*May the next ring stay clear at the top of this list. May each task be small enough to finish and worth the finishing. May what we complete accrete as honest history, and what remains stay light in the hand.*
