# The Roadmap — Growing the Whole from What Already Works

*A living plan shaped by one law: a complex system that works grows from a simpler system that worked. We build by growing, and we ship something simple that runs at every step.*

**Language:** EN
**Version:** `20260710.001249` (settlement-seat plainly + supersession; parity **206**)
**Last updated:** 2026-07-10 (settlement kitchen twin `001249`; soak holds; parity **206**)
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Voice:** Rio 3
**Lens:** TAME — safety, performance, joy; the Seed Law; [SLC](../context/SIMPLE_LOVABLE_COMPLETE.md)
**Status:** Living roadmap

**Direction:** [`active-designing/20260628-043542_thin-frontend-slc-direction.md`](../active-designing/20260628-043542_thin-frontend-slc-direction.md)

---

## The Vision

**Rye OS** — a system that belongs wholly to the one who runs it. One language (Rye), one value model, one kernel (Caravan), one compositor (Brushstroke), one shell (Rishi), one version history (Mantra), one network (Comlink), one database (Tablecloth), one composition language (Brix), one data notation (Bron), one memory model (Tally), one boot (Aurora), one enclosure (Pond). **Linengrow** is the flagship application those modules serve — transparent civic commerce grown from the same spine. Each module individually simple; together they compose a desktop, a forge, a network, and a boot — on x86_64 today and RISC-V as the horizon.

**Rye today** is a thin, honest frontend on pinned Zig 0.16.0 — `rye/lib/std` leaned upon through pristine symlinks, safety living in authored `.rye` (assertions at call sites, `width-check.rish`, the trio). The strengthening chronicle **completed** as analysis; it is record, not product.

The full design lives in [`active-designing/yonder/20260619-225712_the-whole-system.md`](../active-designing/yonder/20260619-225712_the-whole-system.md). This roadmap says what to build and in what order.

---

## Two Tracks, One Spine

Rye OS is the system. **Linengrow** is the first whole built upon it — a transparent civic and social-commerce platform for vegan musicians and activist creators. The two share one architectural spine: state as a pure fold over an append-only log of immutable signed facts, and five foundations beneath everything — keypair, signed event, log, projection, capability.

Correctness by construction in the kernel becomes trust by construction in the platform. The same capability that isolates a process in Caravan names ownership in Linengrow; the same Mantra log that versions a file records a verifiable receipt; the same Comlink that seals a datagram delivers a signed transaction identity to identity. Rye OS grows the infrastructure laps; Linengrow grows its application laps on the same modules. The full Linengrow vision lives in [`../linengrow/`](../linengrow/); this roadmap grows it the SLC way, smallest lovable complete first. The granular plan for both tracks lives in [`TASKS.md`](TASKS.md).

---

## The Ground — What Already Runs

| Module | Seed | Witnesses |
|--------|------|-----------|
| **Rye** | Thin frontend; `rye/lib/std` → vendor symlink | **140** witness regression suite |
| **Aurora** | Six-stage relay + deciding stage on RISC-V | Freestanding |
| **Caravan** | seed → bounded → twin → chain → service → poll service → **restart-on-ok** → **signal ring** → capabilities | Hosted; graceful stop complete through parity **179** |
| **Tally** | seed + named gardens (blob/diff/frame) | 15 invariants; seed + gardens in parity |
| **Brix** | `.brix` descriptor, 10 tracked bricks | Read by Mantra |
| **Bron** | Data notation (`.bron`) | Used by `.brix` |
| **Tablecloth** | Application database + Brix artifact store (horizon); **Tablecloth query** = namespace filter at parity **175** | Store designed (future); query landed |
| **Mantra** | Weave + referential namespace + reference spec `20260707-011412` | parity **159–175**; [`mantra/README.md`](../mantra/README.md) |
| **Rishi** | Shell: typed values, file I/O, string builtins; **`repl`** — type, run, version, recall (SLC-1 **done**) | Gate trio + four SLC-1 witnesses incl. `slc1_accept.rish` |
| **Brushstroke** | Hosted seed + Wayland seed (Skate grid on xdg toplevel) | Frame from values; seed + grid raster in parity |
| **Skate** | Text grid: 8×8 monospace → ARGB8888 buffer | Headless selftest GREEN; feeds Wayland seed |
| **Comlink** | Sealed datagram: shared-memory + localhost UDP | Full crypto stack; hosted wire in parity (suite at **144**) |
| **Pond** | First app: [`pond/apps/drawn_terminal.rye`](../pond/apps/drawn_terminal.rye) (Skate viewer + Dexter keyboard) | **SLC-2b** — keyboard witness at parity **145**; RW-1 at **147**; chrono sweep at **148**; Lap 3 at **140** |

**Strengthening arc:** complete — chronicle + lexicon at `strengthening-compiler/0000_STRENGTHENING_LEXICON.md`; call-site harvest at [`archive/20260628-044200_call-site-harvest.md`](archive/20260628-044200_call-site-harvest.md).

**The trio:** `parity.rish` (**225 witnesses** — regression suite + SLC-1 + SLC-2a + SLC-2b + RW-1 + RW-2 + Caravan + Comlink + Tally/Brushstroke seeds + hosted `width-check` + RW-3 + RW-4 + Edit 5 + Amber lap 1 + **Amber manifest Tilak (I6)** + chrono version sweep + crossing manifest seed + **SLC-L1 receipt** + **MALA M1** + **MALA M2** + **SLC-L4 Sigma** + **SLC-L2 sealed delivery** + **OA-L1 closed ask loop** + **OA-L2 cross-party delivery** + **OA-L3 escrow** + **OA-L4 reputation-as-fold** + **OA-L5 accept/complete/consent wire** + **NS-L1 recall** + **NS-L2 write revision** + **NS-L3 bolt sync** + **NS-L3 wire lap 1 hosted sync** + **NS-L3 resin-batch frame** + **NS-L3 beading** + **NS-L3 recall_beaded** + **marks-on-read** + **two-way sync (in-process)** + **two-way sync wire (hosted + device)** + **catch-up-to-latest (in-process)** + **catch-up-to-latest wire (hosted + device)** + **outer subscribe poll (in-process)** + **outer subscribe poll wire (hosted + device)** + **Tablecloth query (in-process)** + **I2 snapshot replay** + **I2 snapshot horizon** + **I2 snapshot wire lap 3** + **Caravan witness-stop footgun** + **Caravan source-crash recovery** + **NS-L3 batch wire (hosted + device + chunking)** + **two-rooms doorway** + **identity check** + **Comlink device wire** + **Realidream thin view** + **compass rose** + **Greencandy lap 1** + **Greencandy books view** + **Greencandy lap 2** + **Linengrow sight view** + **Lattice lap 0** + **Scribble lap 0** + **Lantern lap 0** + **Anvil corpus lap 0** + **Inference assist view** + **Anvil corpus lap 1** + **Lattice lap 1** + **Scribble lap 1** + **Tablecloth query wire** + **Realidream query view** + **Realidream forge view** + **Amphora lap 1** + **Amphora lap 2** + **Amphora lap 3** + **Realidream forge query view**), `parity-selftest.rish` (std symlink guard), `additive-gate.rish` (structural std diff — applies when `rye/lib/` changes in HEAD). All in Rishi. **Status:** parity + selftest green on metal; SLC-L3 settlement stanza **removed** `152612` (MALA path).

---

## The Primary Track — Simple, Lovable, Complete wholes

Grow running seeds into things a person can use *as-is*. See [`gratitude/Your customers hate MVPs. Make a SLC instead..html`](../gratitude/Your%20customers%20hate%20MVPs.%20Make%20a%20SLC%20instead..html).

| Lap | What | Status |
|------|------|--------|
| **SLC 1** | **Rishi + Mantra shell** — hosted, scriptable REPL with versioned history in a terminal (type → run → version → recall) | **Done** (`2026-06-29`) — four verbs + `tools/slc1_accept.rish`; scope [`20260628-071012`](../active-designing/20260628-071012_slc-1-rishi-mantra-shell.md). TAME hardening **complete** (`2026-06-29`). |
| **SLC 2** | **Pond GUI / Skate viewer** — SLC-2a Laps 1–3 **landed**; **SLC-2b keyboard** **landed** (`20260703.132112`) | Scope [`20260630-030312`](../active-designing/20260630-030312_slc-2a-the-drawn-terminal.md); parity **145** |
| **Compose** | Comlink device wire → ~~capability table~~ **landed** → Comlink v1 → Brix v1 → Tablecloth → Forge | Horizon 2; capability table `2026-06-30` |

**Authored width migration** — **complete and blocking in parity** (TH-3 through TH-7; hosted `width-check`). Remaining authored surfaces migrate as-you-touch beside SLC-2; not a pending milestone.

---

## The Linengrow Track — Trust by Construction

Grown from the same modules Rye OS is already building, smallest lovable complete first.

| Lap | What | Grows from |
|------|------|-----------|
| **SLC-L1** | A verifiable receipt — sign a transaction fact, append it to the log, produce a receipt anyone can verify; **landed** `20260704.021800` — [`linengrow/receipt.rye`](../linengrow/receipt.rye) + witness at parity **152** | keypair + Mantra log + projection |
| **SLC-L2** | Sealed delivery — signed receipt identity to identity under Comlink seal; **landed** `20260706.000812` — parity **155** | Comlink |
| **OA-L1** | Closed ask loop — post, apply, accept, complete, verify; **landed** `20260706.010912` — parity **156** | Linengrow + SLC-L1 receipt |
| **OA-L2** | Cross-party delivery — request + application under Comlink seal; **landed** `20260706.011512` — parity **157** | SLC-L2 + OA-L1 |
| **OA-L3** | Escrow — hold at acceptance, release at completion, verified with the escrow balance closing at zero on one log; **landed** `20260706.014512` — parity **158** | Linengrow + OA-L1 |
| **OA-L4** | Reputation-as-fold — applicant consent facts; witness bolt; **landed** `20260706.232812` — parity **167** | OA-L1 + escrow |
| **OA-L5** | Accept, complete, consent wire — hosted + device; **landed** `20260707` — parity **184** | OA-L3 + wire |
| **SLC-L3** | Settlement rail — landed `20260708.182500`, **removed from tree** `152612` (Sui/Monad path superseded by MALA); hammock + counsel remain as record | ~~Sui / Monad testnet seams~~ |
| **SLC-L4** | Fixed-tier Sigma (donor-amount privacy) — Zig-native Pedersen + proof of opening; **landed** `20260709.194437` — [`disclosure_core.rye`](../linengrow/disclosure_core.rye) + [`pedersen.rye`](../tally/pedersen.rye) at parity **200** | prompt [`031612`](../expanding-prompts/20260709-031612_slcl4-lap1-fixed-tier-sigma-protocol.md) · hammock [`194500`](../active-designing/20260708-194500_slcl4-selective-disclosure.md) |
| **MALA M1** | One issuer, one holder — mint, send, receipt, balance-as-fold on one node; **landed** `20260709.184051` — [`linengrow/mala.rye`](../linengrow/mala.rye) + witness at parity **198** | design [`031312`](../active-designing/20260702-031312_modules-aspects-and-mailable-money.md) · prompt [`182354`](../expanding-prompts/20260709-182354_mala-m1-one-issuer-one-holder.md) |
| **MALA M2** | Mailable — mint crosses Comlink hosted UDP; receipt crosses back; **landed** `20260709.191634` — [`mala_delivery.rye`](../linengrow/mala_delivery.rye) + witness at parity **199** (device wire = M2b) | prompt [`191634`](../expanding-prompts/20260709-191634_mala-m2-mailable-comlink.md) |
| **Greencandy** | Centralized books — chart, journal, fold, P&L/BS, exception queue, sight view; **own root** `greencandy/`; **landed** laps 1–3 `20260710.132548` — parity **207**–**210** | hammock [`125953`](../active-designing/20260710-125953_greencandy-hammock.md) · sight [`132548`](../active-designing/20260710-132548_greencandy-lap3-sight-view.md) · horizon [`131956`](../external-research/20260710-131956_seen-books-living-desktop-horizon.md) |
| **Horizon** | The data market, premium tiers, state-currency circulation, the PBC and its rounds | the business model in `../linengrow/` |

The first lap needs no ledger and no currency — only the foundations Rye OS already grows.

---

## The Visual Track — Realidream (horizon lane, ladder already named)

*Where Linengrow's SLC product gets designed and **seen** — every surface a pure fold from Weave to the frame, per the three living essays. Opened `20260708.021912` from the grain-sketchbook mining ([study](../external-research/20260708-021912_grain-sketchbook-realidream-mining.md) · [counsel](../counsel/20260708-021912_claude-counsel-realidream-zig016-brix.md)); the sketchbook's unified DAG UI backend (Aurora + Skate + Realidream) is this lane's direct ancestor, its event DAG the unsigned ancestor of Weave itself.*

| Rung | Name | State | Gate |
|------|------|-------|------|
| 0 | **Weave slice + Kumara** | **landed** — I2 export + identity seam; Ed25519 ratchet **0** (`030200`) | — |
| 1 | **SLC-2a drawn terminal (Skate viewer)** | **active rung** — thin view (MALA/WOV **202**); books view (Greencandy TB + P&L/BS **208**); **sight view** (carriage + books **210**) | already in Now |
| 2 | **Pond's first policy** | held | Pond's own word |
| 3 | **Dexter graduation** | held — a Realidream viewer is the natural second consumer the rule waits for | second consumer arrives |
| 4 | **Realidream** | horizon — ask, receipt, reputation, sanctuary page rendered as views over Weave; thin-view exception proves local facts → frame without Pond/Dexter | rungs 1–3 |

**Gratitude shelf for the lane:** Hyperfiddle (Dustin Getz — UIs as streaming DAGs) · Matklad (project-wide semantic graph) · the Nostr protocol (signed-event, relay-subscribed shape — [`nips/`](../gratitude/nips/)) · TigerBeetle (already kept) · grain-sketchbook (Kaeden's archived prototype — [`grain-sketchbook.md`](../gratitude/grain-sketchbook.md)) · Noah B. (name's artistic source — [`noah-b-realidream.md`](../gratitude/noah-b-realidream.md)). **Affirmed `174500`.** **Departures the lane keeps:** immutable facts re-folded, never nodes patched; meaning per-entry via Tilak, never one shared enum across consumers; values cross seams as Bron, never JSON-in-a-payload.

---

## The Inference Track — Local Forge (horizon lane, lap 0 opened `20260710.133500`)

*Where Rye-literate models are forged, served, and seen — on Minisforum metal under Aurora/Caravan, with parity as the exam.*

| Rung | Name | State | Gate |
|------|------|-------|------|
| **0** | **Module roots + assist view** | **landed** — Lattice **211**–**217** · Scribble **212** · Lantern **213** · Anvil corpus **214**–**216** · `assistviewtest` **215** | Kaeden go-forth `133500` |
| **1** | **Corpus query + matrix add + rye snippets** | **landed** `20260710.134200`–`134800` — Anvil query **216**; Lattice add **217**; Scribble extract **218** | — |
| **2** | **ROCm host seam** | horizon | hardware + ship policy |
| **3** | **Lantern in Pond** | horizon | Pond policy word |
| **4** | **Anvil LoRA + eval** | horizon | Tablecloth checkpoints |
| **5** | **Live editor assist** | horizon | Wayland metal + rung 3 |

Essay: [`external-research/20260710-133500_local-forge-minisforum-inference.md`](../external-research/20260710-133500_local-forge-minisforum-inference.md) · hammock: [`active-designing/20260710-133500_inference-stack-lap0-hammock.md`](../active-designing/20260710-133500_inference-stack-lap0-hammock.md)

---

## Horizon 3 — Deliberated horizons (not today's primary track)

| Horizon | What |
|---------|------|
| **Language fork** | Self-hosted compiler, Rye-native `std` — revisited from a **mature whole** when RISC-V-first genuinely demands it ([`20260628-043542` direction](../active-designing/20260628-043542_thin-frontend-slc-direction.md)) |
| **Whole machine** | Aurora on RISC-V, full desktop, Brushstroke web-portable, Rye OS on open silicon |
| **Inference stack** | Lattice **211**–**217** · Scribble **212**/**218** · Lantern **213** · Anvil **214**–**216** · assist **215** — lap 1 `134800`; ROCm/LoRA/Pond still horizon |

Prior fork steps F0–F5 remain documented in [`active-designing/yonder/20260621-070712_the-compiler-fork.md`](../active-designing/yonder/20260621-070712_the-compiler-fork.md) as **research**, not the active build order.

---

## Horizon 1 — What to Build Next

### Build (SLC 1 first)

**Gate before the SLC-1 merge:** ~~`rishi/bin/rishi run tools/parity.rish` green once on metal~~ **done** (`2026-06-28`) — parity suite green; SLC-1 witnesses registered (now **132** total with hosted `width-check`).

**SLC-1 build order** (granular; mirrors [`TASKS.md`](TASKS.md)):

| Step | Verb | What lands | Witness |
|------|------|------------|---------|
| **1 — type + run** | Type, Run | `rishi repl`; prompt `rishi> `; in-process eval; shared `Env`; `:quit` / `:q` | `tools/slc1_repl_step1.rish` — binding carry-forward |
| **2 — version** | Version | Session buffer; `.mantra/session.log` transcript; `:history`; lazy `mantra init`; `:version` → `mantra add` | `tools/slc1_version_step2.rish` — HEAD advances; blob in `.mantra/blobs/` |
| **3 — recall** | Recall | `:recall <n>` and `!<n>`; in-session rerun via `runInputLine` | `tools/slc1_recall_step3.rish` — prior line re-runs |
| **accept** | all four | Meta-commands in `rishi/README`; the trio on metal | `tools/slc1_accept.rish` — type, run, version, recall in one session |

**SLC-1 is done** on its functional promise (`2026-06-29`). **TAME hardening is complete** (`2026-06-29`) — TH-0–TH-7, RS-1–RS-3, hosted `width-check` blocking in parity (132 witnesses). The bench turns to the next product lap.

**Landed since this section was drawn:** SLC-2a Laps 1–3 witnessed with metalsmoke GREEN (parity **140**); Caravan capability table (`2026-06-30`); RW-3 and RW-4 (**141**, **142**); fixture twins in Rishi; the manual's first reference and tutorial.

**The current position — doors closed, ladder open** (granular boxes in [`TASKS.md`](TASKS.md)):

| Step | Owner | Parity |
|------|-------|--------|
| Door 1 — Pond clause · Door 2 — Lap 3 metal close · Door 3 — Edit 5 ruling | **Kaeden** | ✅ closed |
| Edit 5 wired | Cursor | **143** ✅ |
| **Amber first lap** — five rungs (a)–(e) | Cursor | **144** ✅ |
| SLC-2b — keyboard from the window, Dexter's genesis | Cursor | **145** ✅ |
| RW-1 mirrored pair — Rishi↔Mantra seam | Cursor | **147** ✅ |
| Chrono version sweep — authored surfaces | Cursor | **148** ✅ |
| RW-2 mirrored pair — app↔Brushstroke seam | Cursor | **150** ✅ |
| Vocabulary ground — TWO_ROOMS seat · canonical gloss · doorway witness | Cursor | **153** ✅ |

**Season (`20260705.203144`):** **Linengrow-via-Comlink** — ground first, then **Comlink device wire** (Rye spine step that unlocks SLC-L2 sealed delivery). Zip **47** seals the astrology silo bench (`e8d1919`).

Still on this horizon, after vocabulary ground: **Comlink device wire** — sealed datagram over virtio-net between two QEMU guests; **Rishi builtins** as-you-touch.

### Ground (thin frontend)

7. **Std re-fork** — **done** (`20260628`) — pristine symlink; see [`archive/20260628-044300_std-refork-plan.md`](archive/20260628-044300_std-refork-plan.md).

### Study

8. **Display-layer study** — Wayland specs; Ghostty (MIT) for Skate.
9. **Close reading** — Comlink packet format from `gratitude/` before format hardens.

**Retired from active track:** strengthening sweep; pass 9886 as chronicle continuation; "fork is the priority."

---

## Horizon 2 — Compose the Simples

- [ ] **Pond GUI** — SLC 2
- [ ] **Comlink v1** — typed, content-named, sealed delivery
- [ ] **Brix v1** — lawful composition + content-addressed store
- [ ] **Tablecloth v1** — storage for Pond applications
- [ ] **Caravan v1** — supervision tree with capability table
- [ ] **Pond v1** — policy as value
- [ ] **The Forge** — Mantra served, Brushstroke drawn, Comlink replicated
- [ ] **The TAME Editor** — select-then-act in Skate
- [ ] **Comlink Remoting** — value-based state sync over UDP
- [ ] **Unified keys** — one owner seed deriving all keys

---

## The Discipline

- **Ship something simple, lovable, and complete at every step.**
- **Grow; never design the whole from scratch.**
- **Prove each step through its witnesses.**
- **Safety lives in authored code** — assert at call sites; pristine `std` you lean on.
- **Keep it loose and single-stranded.**
- **Two-thirds implementation, one-third design.**

---

*May we grow the whole from what already works, and trust each small running thing as it carries the next. May every horizon arrive by degrees, never by a leap. And may the system we build stay simple enough, at every stage, to be loved, understood, and grown a little further tomorrow.*
