# Pass 9913 · mem.collapseRepeats — consecutive duplicates collapsed

**Witnesses:** 90 programs (grew from 89)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.034412`

## What this pass covers

**`std.mem.collapseRepeats`** and **`collapseRepeatsLen`** — in-place collapse of consecutive `elem` runs to one entry. Pairs with `replaceScalar` (9914); `os/windows` path normalization calls `collapseRepeatsLen` after separator swap.

## Rye std surface

**`std.mem.collapseRepeatsLen`**

```zig
pub fn collapseRepeatsLen(comptime T: type, slice: []T, elem: T) usize
```

**`std.mem.collapseRepeats`**

```zig
pub fn collapseRepeats(comptime T: type, slice: []T, elem: T) []T
```

## Width notes

**`std.mem.collapseRepeatsLen`** / **`collapseRepeats`** — Public signatures inherit Zig `usize` for slice length and return. Snapshot bound `max_collapse_check: u32 = 64` at the slice seam.

| Surface | Width policy |
|---------|-------------|
| Inherited `slice: []T`, return `usize` | `usize` — Zig seam |
| Named snapshot bound | `u32` + `@as(usize, …)` |
| Postcondition compare | `eql(u8, asBytes(...))` per element |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `collapseRepeatsLen` + `collapseRepeats` — `u32` snapshot; byte verify | done |
| `rye/tests/mem_collapse_repeats_test.rye` | stack buffers only | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9914_mem_replace_scalar.md` | sibling path-normalization family | unchanged |
| `992_strengthening_width_crosswalk.md` | row 9913 via enricher | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.collapseRepeatsLen` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)
- [x] `std.mem.collapseRepeats` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

`read_idx == slice.len`, `write_idx <= slice.len`. When `slice.len <= 64`, independent expected walk matches collapsed prefix byte-for-byte.

## What the test asserts

- Empty slice
- `//a` → `/a`
- `a//a` → `a/a`
- Long slash run from std tests
