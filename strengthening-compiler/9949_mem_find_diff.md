# Pass 9949 · findDiff — first inequality agrees with equality

**Witnesses:** 54 programs (grew from 53)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.191212`

## What this pass covers

**`std.mem.findDiff`** — index of first differing element, or null when slices are equal. Complements `mem.eql` (9996) and `mem.order` (9953).

## Rye std surface

**`std.mem.findDiff`**

```zig
pub fn findDiff(comptime T: type, a: []const T, b: []const T) ?usize
```

## Width notes

**`std.mem.findDiff`** — Public signature inherits Zig `usize` for slice lengths and indices — keep at the inherited seam per `992` Phase 4. Narrow to `u32`/`u64` only for named bounds inside the body (`max_*_check`, loop counters) with `assert` before `@intCast`.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `findDiff` — inherited `usize` seam; assertions only | done |
| `rye/tests/mem_find_diff_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9949_mem_find_diff.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9949 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.findDiff` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

On every return path:

- `null` ⇒ `eql(a, b)`
- `Some(idx)` ⇒ `idx == @min(a.len, b.len)` when lengths differ, else `a[idx] != b[idx]` with `idx < shortest`

## What the test asserts

- Equal slices, length mismatch at common prefix end, mid-string diff
- Shared-pointer sub-slice vs full slice
