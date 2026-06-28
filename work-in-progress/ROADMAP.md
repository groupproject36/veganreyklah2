# The Roadmap — Growing the Whole from What Already Works

*A living plan shaped by one law: a complex system that works grows from a simpler system that worked. We build by growing, and we ship something simple that runs at every step.*

**Language:** EN
**Version:** `20260628-044300` (thin-frontend direction adopted)
**Last updated:** 2026-06-28
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Voice:** Reya 2
**Lens:** TAME — safety, performance, joy; the Seed Law; SLC
**Status:** Living roadmap

**Direction:** [`active-designing/20260628-043542_thin-frontend-slc-direction.md`](../active-designing/20260628-043542_thin-frontend-slc-direction.md)

---

## The Vision

**Rye OS** — a system that belongs wholly to the one who runs it. One language (Rye), one value model, one kernel (Caravan), one compositor (Brushstroke), one shell (Rishi), one version history (Mantra), one network (Comlink), one database (Tablecloth), one composition language (Brix), one data notation (Bron), one memory model (Tally), one boot (Aurora), one enclosure (Pond). Each module individually simple; together they compose a desktop, a forge, a network, and a boot — on x86_64 today and RISC-V as the horizon.

**Rye today** is a thin, honest frontend on pinned Zig 0.16.0 — `rye/lib/std` leaned upon through pristine symlinks, safety living in authored `.rye` (assertions at call sites, `width-check.rish`, the gate trio). The strengthening chronicle **completed** as analysis; it is record, not product.

The full design lives in [`active-designing/20260619-225712_the-whole-system.md`](../active-designing/20260619-225712_the-whole-system.md). This roadmap says what to build and in what order.

---

## The Ground — What Already Runs

| Module | Seed | Witnesses |
|--------|------|-----------|
| **Rye** | Thin frontend over Zig; pristine `std` (re-fork proposed) | 116 behavior witnesses |
| **Aurora** | Six-stage relay + deciding stage on RISC-V | Freestanding |
| **Caravan** | seed → bounded → twin → chain | Hosted, asserted |
| **Tally** | seed + named gardens (blob/diff/frame) | 15 invariants |
| **Brix** | `.brix` descriptor, 10 tracked bricks | Read by Mantra |
| **Tablecloth** | General-purpose database + object storage | Designed (future) |
| **Bron** | Data notation (`.bron`) | Used by `.brix` |
| **Mantra** | Weave + commit chain + add-all + log | 9/9 bricks wove |
| **Rishi** | Shell: typed values, file I/O, string builtins | Gate trio in `.rish` |
| **Brushstroke** | Hosted seed + Wayland seed (one window) | Frame from values |
| **Skate** | Text grid: 8×8 monospace on Wayland | Headless selftest |
| **Comlink** | Sealed datagram: shared-memory + localhost UDP | Full crypto stack |
| **Pond** | Policy as a value (`pond.rish`) | Designed |

**Strengthening arc:** complete — chronicle + lexicon at `strengthening-compiler/0000_STRENGTHENING_LEXICON.md`; call-site harvest at [`20260628-044200_call-site-harvest.md`](20260628-044200_call-site-harvest.md).

**Gate trio:** `parity.rish` (differential — retires after std re-fork), `parity-selftest.rish`, `additive-gate.rish`. All in Rishi.

---

## The Primary Track — Simple, Lovable, Complete wholes

Grow running seeds into things a person can use *as-is*. See [`gratitude/Your customers hate MVPs. Make a SLC instead..html`](../gratitude/Your%20customers%20hate%20MVPs.%20Make%20a%20SLC%20instead..html).

| Ring | What | Status |
|------|------|--------|
| **SLC 1** | **Rishi + Mantra shell** — hosted, scriptable REPL with versioned history in a terminal (type → run → version → recall) | **Next north star** |
| **SLC 2** | **Pond GUI** — same loop in Brushstroke/Skate window on x86_64 | After Skate text rendering |
| **Compose** | Comlink device wire → capability table → Comlink v1 → Brix v1 → Tablecloth → Forge | Horizon 2 |

**Authored width migration** (Phase 1b: `brushstroke/*` done; **`mantra/*` next**) continues — good Tiger on its own, enforced by `width-check.rish`; **not** fork-work.

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

1. **Rishi + Mantra shell loop** — scriptable hosted shell with versioned history; gates green; terminal-complete.
2. **Rishi builtins** — trim improvements still open.
3. **Width migration Phase 1b** — `mantra/*` next (decoupled from fork).
4. **Caravan capability table** — small Rye struct naming what each child may do.
5. **Comlink device wire** — sealed datagram over virtio-net between two QEMU guests.
6. **Skate text rendering** — unlocks SLC 2 (Pond GUI).

### Ground (thin frontend)

7. **Std re-fork** — pristine symlink; plan at [`20260628-044300_std-refork-plan.md`](20260628-044300_std-refork-plan.md) (proposed; awaits approval).

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
