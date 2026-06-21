# 992 · `usize` Width Baseline — inventory before migration

**Stamp:** `20260621.051312`
**Policy:** `context/TAME_STYLE.md` (Rye supplement) · `gratitude/TIGER_STYLE.md` (Tiger source)
**Charter:** `expanding-prompts/10024_explicit_width_audit.md`
**Fork:** `external-research/967_literal_usize_ban_language_fork.md` · `active-designing/970_explicit_width_in_rye.md`
**Status:** Phase 1b — `caravan/chain` / Skate grid; Phase 4 seam audit on Zig-ground `std` (interim); **Fork F0 decided `051312`**

---

## Strengthening compiler ↔ width (Phase 4)

Every pass in `strengthening-compiler/` now carries:

- **`## Rye std surface`** — live strengthened `pub fn` from `rye/lib/std`
- **`## Width notes`** — inherited `usize` seam vs named `u32`/`u64` bounds
- **`## usize explicit audit`** — Tiger/TAME policy table per surface + witness (`tools/tame_usize_audit.rye`):
  - **Tier C (inherited `std`)** — public `usize` signatures documented, not violations (`10024` rule 3)
  - **`u32` named bounds** — design width (`max_*: u32`), not `usize` (Tiger Style)
  - **Seam widen** — `@as(usize, u32_bound)` at slice compare only
  - **Seam narrow** — `@intCast` paired with `assert` (`10024` rule 2)
  - **`fail`** — `max_*: usize`, authored `usize` fields/params we publish
  - **Tier B witness** — `.rye` test: `usize` only at `buf[0..n]` edge
- **`## Audited surfaces`** — `[x]` / `[ ]` per function (checkmark = zero `fail` in usize audit)
- **`## Width audit (affected files)`** — file table; usize audit + witness must pass for full sign-off

**Auditor:** `tools/tame_usize_audit.rye` — shared by `tools/enrich_strengthening_docs.rye`

**Crosswalk:** `993_strengthening_width_crosswalk.md` (86 passes, auto-indexed)
**Lexicon:** `strengthening-compiler/0000_STRENGTHENING_LEXICON.md` — std-shaped tree with ✅ / `[ ]` audit column (`0000` ceiling · `9999` floor)
**Enricher:** `tools/enrich_strengthening_docs.rye` — re-run after each new `k` pass (updates crosswalk + lexicon)
**Prompt:** `expanding-prompts/10025_strengthening_stdlib_doc_width_pass.md`

Named snapshot bounds in strengthened `mem` (`max_reverse_check`, `max_rotate_check`, `max_replace_*`) are **`u32`** with comparison at the `usize` slice seam — public Zig signatures unchanged.

---

## Summary

| Tier | Meaning | `usize` occurrences (authored `.rye`) | Action |
|------|---------|----------------------------------------|--------|
| **A — Authored programs** | Seeds, tools, Skate, Rishi, Comlink, Caravan, Mantra, Aurora | **~175** across **22** files | Migrate per Phase 1–3 |
| **B — Witness tests** | `rye/tests/*` | **~15** (mostly boundary sweeps) | Keep at slice edge; narrow locals where easy |
| **C — Inherited std** | `rye/lib/std/**/*.zig` | **thousands** (`mem.zig` alone ~185) | Touch only during strengthening passes |
| **D — Vendor / gratitude** | `vendor/`, `gratitude/` | out of scope | Untouched |

**Contradiction resolved:** TAME supplement previously said “array indices and lengths are `usize`.” Tiger Style and `996_TAME_STYLE.md` say the opposite. **`210812` policy:** `u32` / `u64` in APIs we own; `usize` only at inherited slice boundaries.

---

## Authored `.rye` inventory (Tier A)

| File | `usize` hits | Tier tag | Phase | Notes |
|------|-------------|----------|-------|-------|
| `rishi/src/main.rye` | 37 | interpreter | 3 | line indices, eval stack — prefer `u32` with named max depth |
| `brushstroke/skate_grid.rye` | 29 | display | 1 | `cols`/`rows`/pixel loops → `u32`; cast at `[]u8` stride |
| `comlink/hosted_wire.rye` | 12 | wire | 2 | datagram offsets → `u64` / `u32` per frame spec |
| `caravan/chain.rye` | 12 | supervision | 1 | stage indices bounded by chain depth |
| `caravan/twin.rye` | 0 | supervision | 1 | **Done** `020512` |
| `aurora/src/deciding.rye` | 11 | metal | 2 | MMIO offsets → `u64`; small counters → `u32` |
| `aurora/src/posted.rye` | 11 | metal | 2 | mailbox layout — wire widths |
| `aurora/src/relay.rye` | 8 | metal | 2 | relay buffer walks |
| `caravan/bounded.rye` | 0 | supervision | 1 | **Done** `015712` |
| `tally/gardens.rye` | 0 | memory | 1 | **Done** `211712` |
| `brushstroke/wayland_seed.rye` | 9 | display | 1 | SHM stride / dimension casts |
| `mantra/src/main.rye` | 5 | vcs | 1 | line/weave indices |
| `tally/seed.rye` | 0 | memory | 1 | **Done** `211712` |
| `caravan/seed.rye` | 0 | supervision | 1 | **Done** `014512` |
| `rye/src/main.rye` | 2 | tool | 3 | bridge argv |
| `mantra/src/diff.rye` | 2 | vcs | 1 | LCS table indices |
| `aurora/src/wire.rye` | 1 | metal | 2 | |
| `brushstroke/skate_grid_test.rye` | 4 | test | 1 | follows grid types |
| `rye/tests/tally_gardens_test.rye` | 6 | witness | B | |
| `rye/tests/mantra_weave_test.rye` | 2 | witness | B | |
| `rye/tests/sha3_*_boundary_test.rye` | 2 | witness | B | rate sweep — keep `usize` at `buf[0..n]` edge |

*Counts from ripgrep `usize` token scan, `210812`. Re-run before each phase closes.*

---

## Conversion patterns (reference)

**Struct field (before → after):**

```zig
pos: usize,          // today
pos: u32,            // invariant: pos <= buf.len (and buf.len is bounded at init)
```

**Slice loop (boundary cast):**

```zig
var i: u32 = 0;
while (i < @as(u32, @intCast(buf.len))) : (i += 1) {
    assert(i < buf.len);
    ...
}
```

**Narrowing from slice length:**

```zig
assert(buf.len <= std.math.maxInt(u32));
const n: u32 = @intCast(buf.len);
```

---

## Phase checklist

- [x] **Phase 0** — policy, baseline, living docs (`210812`)
- [x] **Phase 1a** — `tally/seed.rye` + `tally/gardens.rye` (`211712`)
- [ ] **Phase 1b** — `caravan/chain` → `brushstroke/skate_grid.rye` (~~seed, bounded, twin~~ done)
- [ ] **Phase 2** — Aurora + Comlink wire layouts
- [ ] **Phase 3** — Rishi interpreter
- [x] **Phase 4 (interim)** — Zig-ground `std` seam audit + strengthen touch (`031812`–`043312`; see `968`)
- [ ] **Phase 5** — `width-audit.rish` in CI

## Language fork checklist (post–`usize` ban — `967` / `970`)

- [x] **F0 — Decide** — literal ban in Rye types; research + siloed design (`051312`)
- [ ] **F1 — Type story** — `[]T` with `u32` len; compiler spike rejects `usize` in `.rye`
- [ ] **F2 — Authored corpus** — zero `usize` in published `.rye`; width gate required
- [ ] **F3 — `rye/lib` rewrite** — Rye-native `std` signatures; witnesses re-based
- [ ] **F4 — Bridge sunset** — self-hosted `rye run` without Zig for our tree
- [ ] **F5 — Guest Zig** — interop lane documented for Rye OS

Phase 4 seam policy **sunsets** when F3 completes. Until then, both tracks run in parallel: finish Zig-ground strengthening green; migrate authored `.rye` toward F2.

---

*May the inventory shrink honestly, one module at a time, with the gate green at every step.*
