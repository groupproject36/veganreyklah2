# The Roadmap — Growing the Whole from What Already Works

*A living plan shaped by one law: a complex system that works grows from a simpler system that worked. We build by growing, and we ship something simple that runs at every step.*

**Language:** EN
**Version:** `20260628-124512` (Linengrow track; two tracks one spine)
**Last updated:** 2026-07-02 (SLC-2a Ring 3 witness; 139 witnesses)
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Voice:** Reya 2
**Lens:** TAME — safety, performance, joy; the Seed Law; [SLC](../context/SIMPLE_LOVABLE_COMPLETE.md)
**Status:** Living roadmap

**Direction:** [`active-designing/20260628-043542_thin-frontend-slc-direction.md`](../active-designing/20260628-043542_thin-frontend-slc-direction.md)

---

## The Vision

**Rye OS** — a system that belongs wholly to the one who runs it. One language (Rye), one value model, one kernel (Caravan), one compositor (Brushstroke), one shell (Rishi), one version history (Mantra), one network (Comlink), one database (Tablecloth), one composition language (Brix), one data notation (Bron), one memory model (Tally), one boot (Aurora), one enclosure (Pond). **Linengrow** is the flagship application those modules serve — transparent civic commerce grown from the same spine. Each module individually simple; together they compose a desktop, a forge, a network, and a boot — on x86_64 today and RISC-V as the horizon.

**Rye today** is a thin, honest frontend on pinned Zig 0.16.0 — `rye/lib/std` leaned upon through pristine symlinks, safety living in authored `.rye` (assertions at call sites, `width-check.rish`, the gate trio). The strengthening chronicle **completed** as analysis; it is record, not product.

The full design lives in [`active-designing/20260619-225712_the-whole-system.md`](../active-designing/20260619-225712_the-whole-system.md). This roadmap says what to build and in what order.

---

## Two Tracks, One Spine

Rye OS is the system. **Linengrow** is the first whole built upon it — a transparent civic and social-commerce platform for vegan musicians and activist creators. The two share one architectural spine: state as a pure fold over an append-only log of immutable signed facts, and five foundations beneath everything — keypair, signed event, log, projection, capability.

Correctness by construction in the kernel becomes trust by construction in the platform. The same capability that isolates a process in Caravan names ownership in Linengrow; the same Mantra log that versions a file records a verifiable receipt; the same Comlink that seals a datagram delivers a signed transaction identity to identity. Rye OS grows the infrastructure rings; Linengrow grows its application rings on the same modules. The full Linengrow vision lives in [`../linengrow/`](../linengrow/); this roadmap grows it the SLC way, smallest lovable complete first. The granular plan for both tracks lives in [`TASKS.md`](TASKS.md).

---

## The Ground — What Already Runs

| Module | Seed | Witnesses |
|--------|------|-----------|
| **Rye** | Thin frontend; `rye/lib/std` → vendor symlink | **139** witness regression suite |
| **Aurora** | Six-stage relay + deciding stage on RISC-V | Freestanding |
| **Caravan** | seed → bounded → twin → chain → **capabilities** | Hosted, asserted; seeds + capabilities in parity |
| **Tally** | seed + named gardens (blob/diff/frame) | 15 invariants; seed + gardens in parity |
| **Brix** | `.brix` descriptor, 10 tracked bricks | Read by Mantra |
| **Tablecloth** | General-purpose database + object storage | Designed (future) |
| **Bron** | Data notation (`.bron`) | Used by `.brix` |
| **Mantra** | Weave + commit chain + add-all + log | 9/9 bricks wove |
| **Rishi** | Shell: typed values, file I/O, string builtins; **`repl`** — type, run, version, recall (SLC-1 **done**) | Gate trio + four SLC-1 witnesses incl. `slc1_accept.rish` |
| **Brushstroke** | Hosted seed + Wayland seed (Skate grid on xdg toplevel) | Frame from values; seed + grid raster in parity |
| **Skate** | Text grid: 8×8 monospace → ARGB8888 buffer | Headless selftest GREEN; feeds Wayland seed |
| **Comlink** | Sealed datagram: shared-memory + localhost UDP | Full crypto stack; hosted wire in parity (**136**) |
| **Pond** | Policy as a value (`pond.rish`) | Designed |

**Strengthening arc:** complete — chronicle + lexicon at `strengthening-compiler/0000_STRENGTHENING_LEXICON.md`; call-site harvest at [`archive/20260628-044200_call-site-harvest.md`](archive/20260628-044200_call-site-harvest.md).

**Gate trio:** `parity.rish` (**139 witnesses** — regression suite + SLC-1 + SLC-2a + Caravan + Comlink + Tally/Brushstroke seeds + hosted `width-check`), `parity-selftest.rish` (std symlink guard), `additive-gate.rish` (structural std diff — applies when `rye/lib/` changes in HEAD). All in Rishi. **Status:** parity + selftest green on metal (`2026-07-02`); additive-gate runs when std changes land.

---

## The Primary Track — Simple, Lovable, Complete wholes

Grow running seeds into things a person can use *as-is*. See [`gratitude/Your customers hate MVPs. Make a SLC instead..html`](../gratitude/Your%20customers%20hate%20MVPs.%20Make%20a%20SLC%20instead..html).

| Ring | What | Status |
|------|------|--------|
| **SLC 1** | **Rishi + Mantra shell** — hosted, scriptable REPL with versioned history in a terminal (type → run → version → recall) | **Done** (`2026-06-29`) — four verbs + `tools/slc1_accept.rish`; scope [`20260628-071012`](../active-designing/20260628-071012_slc-1-rishi-mantra-shell.md). TAME hardening **complete** (`2026-06-29`). |
| **SLC 2** | **Pond GUI / Skate viewer (SLC-2a)** — Rings 1–2 **landed**; Ring 3 witness **landed**; metal confirmation next | Scope [`20260630-030312`](../active-designing/20260630-030312_slc-2a-the-drawn-terminal.md); parity **139** |
| **Compose** | Comlink device wire → ~~capability table~~ **landed** → Comlink v1 → Brix v1 → Tablecloth → Forge | Horizon 2; capability table `2026-06-30` |

**Authored width migration** — **complete and blocking in parity** (TH-3 through TH-7; hosted `width-check`). Remaining authored surfaces migrate as-you-touch beside SLC-2; not a pending milestone.

---

## The Linengrow Track — Trust by Construction

Grown from the same modules Rye OS is already building, smallest lovable complete first.

| Ring | What | Grows from |
|------|------|-----------|
| **SLC-L1** | A verifiable receipt — sign a transaction fact, append it to the log, produce a receipt anyone can verify | keypair + Mantra log + projection |
| **SLC-L2** | Sealed delivery — a signed receipt sent identity to identity, under seal | Comlink |
| **SLC-L3** | Settlement — a transaction settled on Sui with USDsui, verifiable on the ledger | Sui / Mysticeti |
| **SLC-L4** | The selective-disclosure pass — a zero-knowledge credential proving a claim without revealing the data behind it | keypair + Sui ZK foundations |
| **Horizon** | The data market, premium tiers, state-currency circulation, the PBC and its rounds | the business model in `../linengrow/` |

The first ring needs no ledger and no currency — only the foundations Rye OS already grows.

---

## Horizon 3 — Deliberated horizons (not today's primary track)

| Horizon | What |
|---------|------|
| **Language fork** | Self-hosted compiler, Rye-native `std` — revisited from a **mature whole** when RISC-V-first genuinely demands it ([`20260628-043542` direction](../active-designing/20260628-043542_thin-frontend-slc-direction.md)) |
| **Whole machine** | Aurora on RISC-V, full desktop, Brushstroke web-portable, Rye OS on open silicon |
| **Inference stack** | Lantern, Lattice, Anvil — after the living desktop composes |

Prior fork steps F0–F5 remain documented in [`active-designing/20260621-070712_the-compiler-fork.md`](../active-designing/20260621-070712_the-compiler-fork.md) as **research**, not the active build order.

---

## Horizon 1 — What to Build Next

### Build (SLC 1 first)

**Gate before the SLC-1 merge:** ~~`rishi/bin/rishi run tools/parity.rish` green once on metal~~ **done** (`2026-06-28`) — parity suite green; SLC-1 witnesses registered (now **132** total with hosted `width-check`).

**SLC-1 build order** (granular; mirrors [`TASKS.md`](TASKS.md)):

| Step | Verb | What lands | Witness |
|------|------|------------|---------|
| **1 — type + run** | Type, Run | `rishi repl`; prompt `rishi> `; in-process eval; shared `Env`; `:quit` / `:q` | `tools/slc1_repl_step1.rish` — binding carry-forward |
| **2 — version** | Version | Session buffer; `.mantra/session.log` transcript; `:history`; lazy `mantra init`; `:version` → `mantra add` | `tools/slc1_version_step2.rish` — HEAD advances; blob in `.mantra/blobs/` |
| **3 — recall** | Recall | `:recall <n>` and `!<n>`; in-session ring via `runInputLine` | `tools/slc1_recall_step3.rish` — prior line re-runs |
| **accept** | all four | Meta-commands in `rishi/README`; gate trio on metal | `tools/slc1_accept.rish` — type, run, version, recall in one session |

**SLC-1 is done** on its functional promise (`2026-06-29`). **TAME hardening is complete** (`2026-06-29`) — TH-0–TH-7, RS-1–RS-3, hosted `width-check` blocking in parity (132 witnesses). The bench turns to the next product ring.

1. **SLC-2a Ring 3** — mirror live Rishi session in the Skate viewer. *Check in with Claude for witness shape and SLC-1 loop wiring before bench.*
2. ~~**Caravan capability table**~~ — **landed** (`2026-06-30`): `caravan/capabilities.rye`; witness in parity at **135**.
3. **Comlink device wire** — sealed datagram over virtio-net between two QEMU guests.
4. **Rishi builtins** — trim improvements still open (optional, as-you-touch).

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
- **Prove each step through the gates.**
- **Safety lives in authored code** — assert at call sites; pristine `std` you lean on.
- **Keep it loose and single-stranded.**
- **Two-thirds implementation, one-third design.**

---

*May we grow the whole from what already works, and trust each small running thing as it carries the next. May every horizon arrive by degrees, never by a leap. And may the system we build stay simple enough, at every stage, to be loved, understood, and grown a little further tomorrow.*
