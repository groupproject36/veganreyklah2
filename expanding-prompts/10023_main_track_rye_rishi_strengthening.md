# 10023 · Main Track — Rye, Rishi, and Strengthening

*Expanded at `044412`: the highest-priority build threads from `995` and `996`, gathered into one runnable prompt now that `10010` is reserved and Tablecloth prose lives in `10018`–`10022`. **⅔ implementation · ⅓ design** (`10017`) — Skate first, then strengthening, then Rishi as gates need.*

**Language:** EN
**Version:** `20260620.044412` (Rye chronological stamp)
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Voice:** Reya 2
**Lens:** TAME — Gall's Law; gate trio; `983` map; `998` strengthening charter

---

## The Seed

> Replace removed prompt slots with work aligned to the most important task list. Reserve `10010`; next prompt takes the highest number.

## Main Track (ordered)

| Priority | Thread | Prompt anchor | Green when |
|----------|--------|---------------|------------|
| **1** | **Skate text grid** — monospace glyphs on `wayland_seed` | `10012` (display), `10017` Track B | One grid of cells draws in the Wayland window |
| **2** | **Strengthening series** — next `std` surface through gate trio | `9999_STRENGTHENING`, `9988`+ | Corpus stays 16/16 GREEN; new `9987_*` log written |
| **3** | **Rishi builtins** — as gates and Pond policy need them | `10017`, `rishi/README` | One family + one `.rish` test per run |
| **4** | **TAME assertion backlog** — fix as code is touched | audit list | Assertions land beside code we edit |
| **5** | **Explicit-width migration** — `usize` → `u32`/`u64` in authored `.rye` | `10024`, `992` | One module migrated; parity green |

**After main track holds green:**

| Thread | Anchor |
|--------|--------|
| Explicit-width migration (`usize` audit) | `10024`, `992` |
| Comlink virtio-net device wire | `10016` |
| Caravan capability table | `984` step 5 |
| Tablecloth v1 store seed | `10022` (deferred until 1–3 stay green) |

## This Run — Pick One

**Track A — Skate (`10017` B)**

- Deliverable: glyph grid on `brushstroke/wayland_seed.rye` — cell model, monospace font bitmap or minimal raster, Frame → buffer
- Design: `980`, `981`, `988`
- Gall: one row of readable text before scroll or input

**Track B — Strengthening**

- Read `strengthening-compiler/9999_STRENGTHENING.md`; choose the next `std` surface Rye/Rishi/Mantra lean on
- Strengthen with TAME assertions; run `tools/parity.rish`; record `9987_*` or next countdown doc

**Track C — Rishi**

- One builtin family gates need next (strings done: `length`, `trim`, `slice`)
- One test file; parity green before compose

## Discipline

- One track per session; green before braid
- Update `995`, `996` when a milestone closes
- Session log; commit when green

## Cross-Links

| Retired / reserved | Lives in |
|--------------------|----------|
| `10010` | Reserved stub only |
| Store + Brix compose | `10018`–`10022` |
| Display frontier (Wayland seed) | `10012` — Skate grows from its green frame |
| Build catches design ratio | `10017` |

---

*May Rye grow surely, Rishi script the gates, and strengthening earn each surface before the next layer composes.*
