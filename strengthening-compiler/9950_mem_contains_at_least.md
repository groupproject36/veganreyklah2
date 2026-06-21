# Pass 9950 · containsAtLeast — threshold tally agrees with scan bounds

**Witnesses:** 53 programs (grew from 52)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.185712`

## What this pass covers

**`std.mem.containsAtLeast`** and **`containsAtLeastScalar2`** — true when a needle or scalar appears at least N times (non-overlapping for needles). Pairs with `mem.count` (9951).

## Rye std surface

**`std.mem.containsAtLeast`**

```zig
pub fn containsAtLeast(comptime T: type, haystack: []const T, expected_count: usize, needle: []const T) bool
```

## Width notes

**`std.mem.containsAtLeast`** — Public signature inherits Zig `usize` for slice lengths and indices — keep at the inherited seam per `992` Phase 4. Narrow to `u32`/`u64` only for named bounds inside the body (`max_*_check`, loop counters) with `assert` before `@intCast`.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `containsAtLeast` — inherited `usize` seam; assertions only | done |
| `rye/tests/mem_contains_at_least_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9950_mem_contains_at_least.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9950 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.containsAtLeast` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

**containsAtLeast** — same in-loop bounds as count; on return:

- `true` ⇒ `found >= expected_count`
- `false` ⇒ `found < expected_count`

**containsAtLeastScalar2**:

- `true` ⇒ `found >= minimum` and `found <= list.len`
- `false` ⇒ `found < minimum` and `found <= list.len`

## What the test asserts

- Scalar and multi-byte thresholds, met and unmet
- Non-overlapping `radar` case
- `containsAtLeastScalar2` on `adadda`
