# Pass 9914 · mem.replaceScalar — in-place scalar swap verified

**Witnesses:** 89 programs (grew from 88)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.033712`

## What this pass covers

**`std.mem.replaceScalar`** — replace every `match` scalar in a mutable slice with `replacement`. Pairs with the replace trio (9915–9917); `std` path normalization uses it (`zip`, `tar`, `os/windows`).

## Rye std surface

**`std.mem.replaceScalar`**

```zig
pub fn replaceScalar(comptime T: type, slice: []T, match: T, replacement: T) void
```

## Width notes

**`std.mem.replaceScalar`** — Public signature inherits Zig `usize` for slice length. Snapshot bound `max_replace_scalar_check: u32 = 64` at the slice seam.

| Surface | Width policy |
|---------|-------------|
| Inherited `slice: []T` | `usize` — Zig seam |
| Named snapshot bound | `u32` + `@as(usize, …)` |
| Postcondition compare | `eql(u8, asBytes(...))` for any `T` |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `replaceScalar` — `u32` snapshot; byte-level postconditions | done |
| `rye/tests/mem_replace_scalar_test.rye` | stack buffers only; no authored `usize` fields | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9915_mem_replace_owned.md` | replace family sibling | unchanged |
| `992_strengthening_width_crosswalk.md` | row 9914 via enricher | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.replaceScalar` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

When `slice.len <= 64`, snapshot before mutation; after loop each index is either `replacement` (was `match`) or unchanged (`eql(u8, asBytes(...))`).

## What the test asserts

- Path separator `\\` → `/`
- All-`x` → all-`y`
- `i32` selective replacement
