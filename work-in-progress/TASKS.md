# Tasks — The Granular Plan

**Language:** EN
**Last updated:** 2026-07-02 (design sitting `20260702.031312`; live rung unchanged)
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Voice:** Reya 2
**Lens:** TAME — safety, performance, joy; SLC; Gall's Law

*This is the living, granular plan — the bench where the current rings are shaped. `ROADMAP.md` holds the why and the order; this file holds the what-now. It is **edited in place**: a task is checked when it lands, and the record of how it landed accretes in `../session-logs/`. Checked items are swept to a session log and pruned here when a section grows heavy. What is next lives here; what happened lives there.*

**Legend:** `[ ]` to do · `[~]` in flight · `[x]` done, pending sweep to a session log.

**Tracks:** **Rye OS** grows the system. **Linengrow** grows the first whole built on it. **Ground** is the shared discipline beneath both.

**Landed through 2026-06-30** (detail in `../session-logs/`): SLC-2a Rings 1–2 (`5b3a5a4`); yonder pass nine; Caravan path + Comlink hosted wire (`dc26396`→`8d720c6`); Tally/Brushstroke foundation seeds in parity (**138**); prior: SLC-1; TAME hardening.

---

## Now — In Flight and Immediate

### Rye OS
- [ ] **SLC-2a — the Skate viewer (drawn terminal)** — scope: [`active-designing/20260630-030312_slc-2a-the-drawn-terminal.md`](../active-designing/20260630-030312_slc-2a-the-drawn-terminal.md). **Rings 1–3 witness landed** — parity **140**; **metalsmoke GREEN** ([`tools/slc2a_ring3_metal.rish`](../tools/slc2a_ring3_metal.rish)). **Ring 3 metal close (Kaeden)** — interactive idle, ceiling, `:quit` on `pond/bin/drawn-terminal`. **SLC-2b placed** — [`20260702-030112_cursor-slc-2b-keyboard-from-window.md`](../expanding-prompts/20260702-030112_cursor-slc-2b-keyboard-from-window.md), awaits nod.

### Linengrow
- [ ] **SLC-L1 scope note** — the hammock spec: the transaction fact, the keypair that signs it, the append to the log, the receipt as a pure fold, the verification. Draw the edge of complete; name what is out (settlement, the market).

### Ground
- [ ] **Kernel-direction memo** — graduate the microkernel leaning in `expanding-prompts/20260628-120912_*` into its own direction memo beside `20260628-043542`, when it feels fully settled. Same pattern as thin-frontend: deliberate, then record.
- [ ] **Amber first ring (horizon)** — designed in [`context/specs/20260701-221512_amber-functional-spec.md`](../context/specs/20260701-221512_amber-functional-spec.md); seal one directory to one drive, one signed record, one verifying fold, one hand-verified golden when the season comes.
- [ ] **Deep-archive hardware (horizon)** — rack, powered dock, bare enterprise drives, front-door tunnel; researched in [`external-research/20260701-213412_deep-archive-and-sovereign-host-blueprint.md`](../external-research/20260701-213412_deep-archive-and-sovereign-host-blueprint.md); procurement waits on the dedicated machine.

**Recorded rulings (`20260701-221512` docs round):** **Amber invocation** — explicit shell command with manual sandbox-key unlock; the docked bare drive is precondition, never trigger; the shell may notice and offer, never act; scrub runs cold, key warm only for the seconds of seal. **Amber key custody** — master `0646 2132 D3E6 3B83 4F97 6E03 A81D 720B 9235 FA7A` cold and certifying; sandbox `DBF8 5343 7A93 7B4E 36B9 3611 D949 807A C26B 2B99` signing and revocable; drive passphrase on paper in the firebox and offsite; any other fingerprint is an error on sight.

---

## Next — Horizons and Optional

### Modules, money, and the manual — horizons (`2026-07-02`)

Ground: [`active-designing/20260702-031312_modules-aspects-and-mailable-money.md`](../active-designing/20260702-031312_modules-aspects-and-mailable-money.md) · named companion: [`external-research/20260702-031312_settlement-consensus-and-many-roads.md`](../external-research/20260702-031312_settlement-consensus-and-many-roads.md).

- [x] **Module/aspect vocabulary** — definitions and graduation rule in the design sitting and [`context/LEXICON.md`](../context/LEXICON.md) pattern section.
- [ ] **Weave graduation trigger (recorded)** — the day Comlink serves named data straight from Weave, `mantra/src/weave.rye` graduates to `weave/` and Mantra imports it like everyone else.
- [ ] **MALA M0 (design ring)** — token-fact shapes and witnesses on paper; opens after the Edit 5 ruling and Amber's first ring, in that order; ladder M0–M4 in the memo.
- [ ] **Digital land = M3 (design only)** — plots as name-claim facts with extent in Realidream's graph, deeds bound to Kumara holders, traded in MALA; ordinary internet and dock-wire alike.
- [ ] **Mycelium gate (recorded)** — the ordering aspect opens at M4's many-issuer season, never before.
- [ ] **Road-keeper (exploration → first ring)** — Comlink's multipath aspect: per-road bounded queues and scorecards; first ring = one session surviving across two UDP paths under QEMU.
- [ ] **Amber-compatibility contract (design)** — export / verify / restore for every log-bearing module (Mantra, Tablecloth, Linengrow, Realidream, MALA); first ring = a Mantra log slice sealed and restored, riding Amber's first ring.
- [ ] **Brix packaging (first ring visible)** — one content-addressed, Kumara-signed package: descriptor read, stones fetched by digest over Comlink, verified on two paths, placed, run in Pond; `.bron` as the resolved-record carrier awaits Kaeden's affirmation.
- [x] **Opening lines (canonized)** — three-line head in TAME guidance; **`tools/opening_lines_witness.rish`** in parity **140**.
- [ ] **Manual program (horizon)** — four rooms: tutorials (Radiant beginner series for Rye and Rishi, tutorials-first because they teach only what runs), task guides, numbered reference specifications (beginning with Aurora, Tally, and Caravan interfaces), and the essays; shape note before any lane is founded.
- [ ] **Pond clause (Kaeden completes)** — *"Pond be the module which has an aspect which becomes the solution for the aspect that we need to —"* Recommended completion: **run what Brix composes under policy** — Pond's **enclosure aspect** as packaging's runtime target; awaiting your true ending.

### Comlink and the long run — horizons (`2026-07-02`)

Ground: [`external-research/20260702-014112_comlink-beyond-dns-and-sockets.md`](../external-research/20260702-014112_comlink-beyond-dns-and-sockets.md) · counsel: [`20260702-014112_horizons-and-blind-spots.md`](20260702-014112_horizons-and-blind-spots.md).

- [x] **Wire hardening (precedes any real peer)** — hosted wire: witness fixture key seeds (replacing `0xA1`/`0xB0`), unique nonce per seal via monotonic counter + SHA3 mix; parity **138** green. Production CSPRNG nonces remain horizon.
- [ ] **Algorithm tags (accretion)** — every signed record carries its algorithm field, so eras verify side by side on one log forever.
- [ ] **Hybrid key agreement (horizon)** — X25519 joined with ML-KEM-768 on the wire; harvest-now-decrypt-later answered.
- [ ] **Dual signatures for the long dark (horizon)** — Amber adds SLH-DSA beside Ed25519 through the OpenPGP seam as its tooling settles.
- [ ] **The stream lane (exploration → first ring)** — bounded, drop-late encrypted datagrams beside the fact lane; WebTransport at the browser seam; relay shape at the front door; codecs stay host seams.
- [ ] **Names without DNS (design only)** — name-claim fact shape, petnames above, Linengrow settlement as the market; no code before Kumara signs.
- [ ] **Setu ruling (Kaeden)** — the USB-C dock-wire lane's name; candidate proposed for the lexicon's open table; first ring = one Comlink datagram over CDC-NCM, host to QEMU guest.
- [ ] **Mantrapod module map (Kaeden affirms)** — the pod's module-by-module plan as tabled in the counsel memo.
- [ ] **Two-oracle sky gate (optional)** — a `.rish` witness around `cast_a_chart.py` asserting agreement against a hand-pinned golden chart.
- [ ] **Intakes awaiting Kaeden's hand** — the mathematics writings (silo together, then weigh against TAME's goals); the Cerebras and wafer-memory silos (held for the inference season).
- [ ] **Recovery rehearsal (after Amber's first ring)** — restore a directory from a cold drive and recover from a revoked sandbox key, so recovery is a witnessed fact.

### TAME hardening — complete (`2026-06-29`)

Record: `session-logs/20260629-204910_th7-width-gate-yonder-convention.md` and prior TH/RS logs. Hosted `width-check` blocks in parity (**138** witnesses).

**Horizon and optional (still open):**

- [ ] **Aurora invariant notes (optional)** — say-why rationales beside `catch unreachable` in `aurora/src/seed.rye`; freestanding only; no width or assert lint.

- [ ] **Mantra CRDT weave (horizon)** — merge-always-succeeds-and-converges semantics from `external-research/yonder/20260617-195312_mantra.md`; SLC-1 seed uses LCS line weave only today.

- [ ] **TAME hygiene (as-you-touch)** — assertion-density backlog, `// invariant:` prefix, and bare `print(...)` via `const print = std.debug.print` in older hosted `.rye`; address when each file is touched, not as a sweep.

- [ ] **Content-centric Rishi messenger (horizon)** — smallest IRC-meets-Dojo CLI over sealed, content-named datagrams; from `expanding-prompts/yonder/20260618-212012_content-centric-messaging.md`; Aurora/Comlink carry the networking seeds today.

- [ ] **Shape-casting for RISC-V bytecode (horizon)** — prove raw bytes match a declared type before trust; draw the shape-vs-execution seam plainly; from the same consumed prompt.

- [ ] **Ownerboot sovereignty (horizon)** — owner-key-sealed boot chain inverting trust at the reset vector; from `external-research/yonder/20260617-195612_ownerboot-riscv-caravan.md`; Caravan is live, the firmware path is horizon.

- [ ] **Unified identity and fractal address space (horizon)** — one seed deriving SSH, GPG, Sui, and Nostr keys; fractal address space shaped by Vedic whole-sign astrology (galaxy / star / planet); ties to Linengrow portable identity; from `expanding-prompts/yonder/20260618-215512_unified-keys-and-address-space.md`; Comlink carries the networking half today.

---

## Soon — Medium Term

### Rye OS
- [ ] **SLC-2 — Pond GUI** — the Rishi+Mantra loop in a Brushstroke/Skate window on x86_64. Simple, lovable, complete at a small scope.
- [ ] **Comlink device wire** — sealed datagram over virtio-net between two QEMU guests. **Hosted wire** in parity; **Caravan seeds** (`seed`→`chain`) in parity at **137**; **Track A** virtio-net bring-up remains.
- [ ] **Comlink v1** — typed, content-named, sealed delivery between identities.
- [ ] **Brix v1** — a `.brix` course evaluating into a closure of content-addressed bricks in Tablecloth, per `active-designing/20260628-120912_brix-the-composer.md`.
- [ ] **Unified keys** — one owner seed deriving all keys.
- [ ] **Revitalization pass** — refresh the oldest active-designing briefs to the current direction; affirmed canonical files get the four-in-one touch (de-number, re-date, affirm, light freshen) rather than rename; see `ORGANIZING.md`.

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

- **Tablecloth horizon** — datastore + layout cluster now in `external-research/yonder/` and `expanding-prompts/yonder/`; shape when SLC bench allows.
- **sixos/s6 infrastructure horizon** — study in `external-research/yonder/20260619-225212_s6-sixos-nix-infuse.md`; Caravan inherits supervision discipline when we reach for it.
- **Bron** — proposed; role beside Brix still open. Brix describes *what a system is made of*; the `.bron` notation brief exists — what does Bron describe alongside it? *(Open ruling for Kaeden.)*
- **Tablecloth** — proposed layout or structured-view layer; named, not yet shaped.
- **`.brush`** — surface-description extension for the day Brushstroke becomes a small language; horizon only.
- **Dexter / Kumara as modules** — names given; whether each earns a full module home is open.
- **Two-backend seam** — Wayland SHM to Mutter now (hosted); framebuffer-to-QEMU sovereign sibling named, not built. *(Pending Kaeden nod.)*
- **Weave** — aspect of Mantra today (`mantra/src/weave.rye`); graduation trigger recorded in [`20260702-031312`](../active-designing/20260702-031312_modules-aspects-and-mailable-money.md).
- **Research essays (authored, living)** — [`external-research/20260630-030312_the-interface-as-a-fold.md`](../external-research/20260630-030312_the-interface-as-a-fold.md); [`external-research/20260630-030312_after-victor-immediate-contact.md`](../external-research/20260630-030312_after-victor-immediate-contact.md); [`external-research/20260630-030312_the-hot-loop-as-the-forge.md`](../external-research/20260630-030312_the-hot-loop-as-the-forge.md).
- **Lotus** — DAW direction adopted in `active-designing/20260630-014012_lotus-the-daw.md`; REAPER docs and AP Mastering design in `gratitude/`; bench waits for SLC-2a.
- **Kernel-direction brief held** — `expanding-prompts/20260628-120912_kernel-direction-brix-and-foundations.md` stays one level deep pending the kernel-direction memo (live Now task).
- **Linengrow's home** — does Linengrow stay a folder in this repo, or graduate to its own repo (`xwb122m/linengrow-*`) once its first ring runs?
- **SLC-L1 and Sui** — confirm the first Linengrow ring uses pure foundations (keypair + log + projection) with no Sui, settlement deferred to SLC-L3. (Recommended: yes.)
- **Brix and Silo** — `infuse.nix` once seeded a "Silo" configuration language; Brix is now the composer. Is Silo retired into Brix, or a distinct config layer? Worth one clear line.
- **TASKS naming** — keep `TASKS.md`, or rename to the warmer `WORKBENCH.md`?
- **OCuLink companion memo** — blueprint [`20260701-213412`](../external-research/20260701-213412_deep-archive-and-sovereign-host-blueprint.md) awaits the server-workstation research memo; bridge into `external-research/` when Kaeden supplies it.
- **Designed-not-built spec bound (Edit 5)** — pending Kaeden ruling: at most one functional spec in designed-not-built flight until its first ring runs green.
- **Birth-chart craft** — siloed library, templates, sample reading, and caster at [`classical-vedic-astrology/`](../classical-vedic-astrology/README.md) (`studies/`, `20260701-232912_*`, `cast_a_chart.py`).

---

*May the next ring stay clear at the top of this list. May each task be small enough to finish and worth the finishing. May what we complete accrete as honest history, and what remains stay light in the hand.*
