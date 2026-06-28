# 996 · The Roadmap — Growing the Whole from What Already Works

*A living plan shaped by one law: a complex system that works grows from a simpler system that worked. We build by growing, and we ship something simple that runs at every step.*

**Language:** EN
**Version:** `20260623.033012` (Rye chronological stamp)
**Last updated:** 2026-06-23
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Voice:** Reya 2
**Lens:** TAME — safety, performance, joy; the Seed Law
**Status:** Living roadmap

---

## The Vision

**Rye OS** — a system that belongs wholly to the one who runs it. One language (Rye), one value model, one kernel (Caravan), one compositor (Brushstroke), one shell (Rishi), one version history (Mantra), one network (Comlink), one database (Tablecloth), one composition language (Brix), one data notation (Bron), one memory model (Tally), one boot (Aurora), one enclosure (Pond). Each module individually simple; together they compose a desktop, a forge, a network, and a boot — on x86_64 today and RISC-V as the horizon.

Rye is its own language — not a Zig derivative forever. The compiler fork is the primary track: no `usize`, `u32` slice lengths, self-hosted compiler, Rye-native std (`967`, `970`).

The full design lives in `active-designing/20260619-225712_the-whole-system.md`. This roadmap says what to build and in what order.

---

## The Ground — What Already Runs

| Module | Seed | Witnesses |
|--------|------|-----------|
| **Rye** | Self-hosting compiler, strengthened std | 90 parity GREEN |
| **Aurora** | Six-stage relay + deciding stage on RISC-V | Freestanding |
| **Caravan** | seed → bounded → twin → chain | Hosted, asserted |
| **Tally** | seed + named gardens (blob/diff/frame) | 15 invariants |
| **Brix** | `.brix` descriptor, 10 tracked bricks | Read by Mantra |
| **Tablecloth** | General-purpose database + object storage | Designed (future) |
| **Bron** | Data notation (`.bron`) — plain key-value, token-efficient | Used by `.brix` |
| **Mantra** | Weave + commit chain + add-all + log | 9/9 bricks wove |
| **Rishi** | Shell: typed values, file I/O, `lines`, `starts-with`, `split`, `join`, `trim`, `slice`, `ends-with`, `contains`, `index-of` | Gate trio in `.rish` |
| **Brushstroke** | Hosted seed + Wayland seed (one window) | Frame from values |
| **Skate** | Text grid: 8×8 monospace on Wayland | Headless selftest |
| **Comlink** | Sealed datagram: shared-memory + localhost UDP | Full crypto stack |
| **Pond** | Policy as a value (`pond.rish`) | Designed |

**Strengthening:** 116 witnesses through the parity gate, all GREEN. Lexicon at `0000_STRENGTHENING_LEXICON.md`.

**Gate trio:** `parity.rish` (behavior), `parity-selftest.rish` (proves RED), `additive-gate.rish` (shape). All in Rishi; no sh fallbacks.

---

## The Primary Track — Fork Rye from Zig

The compiler fork is the destination. Everything else serves it or runs beside it.

| Step | What | Status |
|------|------|--------|
| **F0** | Decide: literal `usize` ban in Rye types | Done |
| **F1** | Compiler spike: reject `usize` in one witness | Next |
| **F2** | Authored corpus: zero `usize` in published `.rye` | In progress — Phase 1b: `brushstroke/*` done; next `mantra/*` |
| **F3** | Rye-native std: `rye/lib` with `u32`/`u64` signatures | After F2 |
| **F4** | Bridge sunset: self-hosted `rye run` without Zig | After F3 |
| **F5** | Guest Zig: interop lane for third-party code | After F4 |

The 90 parity witnesses are the specification F3 satisfies. The seam migration (Phases 1–5 in `992`) runs in parallel with F1–F2.

---

## Horizon 1 — What to Build Next

Ordered by leverage. Each grows from what already runs.

### Build

1. **Rishi builtins** — `if/then/else` and `for-each` landed (`063112`); trim improvements still open.
2. **Skate text rendering** — grow the glyph grid into a usable terminal. Text on screen unlocks the Pond GUI.
3. **Caravan capability table** — small Rye struct naming what each child may do (`984` step 5). The step toward the microkernel.
4. **Comlink device wire** — sealed datagram over emulated `virtio-net` between two QEMU guests. The real network rung.
5. **Width migration** — Phase 1b: `brushstroke/*` done (`235812`); next `mantra/*`.

### Strengthen

6. **Continue the series** — prioritize functions the next code needs (Wayland helpers, UDP ops, text rendering primitives). Quality over quantity. Each pass includes width audit.
7. **Fix the enricher** — `tools/enrich_strengthening_docs.rye` grabs wrong functions by bare name. Match by full module path; re-run on all 86 docs.

### Study

8. **Display-layer study** — Wayland protocol specs for Brushstroke. Ghostty (MIT) for Skate. River through public docs only (GPL-3.0).
9. **Close reading** — packet format, commit rule, relay protocols from `gratitude/` before Comlink's format hardens.

---

## Horizon 2 — Compose the Simples

Each milestone is *made of* the working seeds above.

- [ ] **Pond GUI** — Rishi REPL + Mantra in a Brushstroke/Skate window on x86_64 AMD
- [ ] **Comlink v1** — typed, content-named, sealed message delivery between identities
- [ ] **Brix v1** — lawful composition combinator with its own content-addressed build store (like Nix's `/nix/store`)
- [ ] **Tablecloth v1** — general-purpose database + object storage for Pond applications (our MySQL/Postgres/Turbopuffer)
- [ ] **Caravan v1** — supervision tree with capability table
- [ ] **Pond v1** — Caravan isolation + Tally bounds as a policy value
- [ ] **The Forge** — Mantra served, Brushstroke drawn, Comlink replicated (`982`)
- [ ] **The TAME Editor** — select-then-act in Skate, Brix settings, Rishi behavior (`980`)
- [ ] **Comlink Remoting** — value-based state sync over UDP, roaming by key (`979`)
- [ ] **Unified keys** — one owner seed deriving all keys

---

## Horizon 3 — The Whole Machine

- [ ] **Rye, self-hosted** — own compiler, own std, own width model, RISC-V first-class
- [ ] **The full family** — every module composing through one value model
- [ ] **The desktop** — Brushstroke compositor, Skate terminal, Rishi keybindings (`981`)
- [ ] **Aurora on RISC-V** — verified boot from owner key to living system
- [ ] **Brushstroke, web-portable** — `wasm32-freestanding` backend
- [ ] **Rye OS** — the whole machine on open silicon, belonging wholly to the one who runs it

---

## The Discipline

- **Ship something simple that runs at every step.**
- **Grow; never design the whole from scratch.**
- **Prove each step through the gates.**
- **Keep it loose and single-stranded.**
- **The fork is the priority — Rye becomes its own language.**
- **Two-thirds implementation, one-third design.**

---

*May we grow the whole from what already works, and trust each small running thing as it carries the next. May every horizon arrive by degrees, never by a leap. And may the system we are building stay simple enough, at every stage, to be loved, understood, and grown a little further tomorrow.*
