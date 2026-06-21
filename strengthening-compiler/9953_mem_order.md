# Pass 9953 · mem.order — lexicographic order agrees with equality

**Witnesses:** 50 programs (grew from 49)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.182812`

## What this pass covers

**`std.mem.order`** and **`lessThan`** — lexicographic compare on slices. Backs `SemanticVersion` pre-release ordering and general string sorting.

## Rye std surface

**`std.mem.order`**

```zig
pub fn order(lhs: Alignment, rhs: Alignment) std.math.Order
```

## Width notes

**`std.mem.order`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `order` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/mem_order_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9953_mem_order.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9953 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.order` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

**order** — on every return path:

- `.eq` ⇒ `eql(lhs, rhs)`
- `.lt` / `.gt` ⇒ `!eql(lhs, rhs)`

**lessThan** — when true, slices are not equal.

## What the test asserts

- Less, equal, greater by content and by length prefix
- Shared-pointer sub-slice vs full slice
- `lessThan` mirrors `order == .lt`
