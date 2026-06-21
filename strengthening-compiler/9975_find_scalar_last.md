# Pass 9975 · findScalarLast — last match stays in-range at the sought value

**Corpus:** 28 programs (grew from 27)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.162712`

## What this pass covers

**`std.mem.findScalarLast`** (`lastIndexOfScalar`) — linear search for the last occurrence of a scalar in a slice. Backs `path.extension` and `path.stem`; pairs with `findScalar` (9996).

## Rye std surface

**`std.mem.findScalarLast`**

```zig
pub fn findScalarLast(comptime T: type, slice: []const T, value: T) ?usize
```

## Width notes

**`std.mem.findScalarLast`** — Public signature inherits Zig `usize` for slice lengths and indices — keep at the inherited seam per `992` Phase 4. Narrow to `u32`/`u64` only for named bounds inside the body (`max_*_check`, loop counters) with `assert` before `@intCast`.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `findScalarLast` — inherited `usize` seam; assertions only | done |
| `rye/tests/find_scalar_last_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9975_find_scalar_last.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9975 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.findScalarLast` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postcondition

On return when a match is found:

```zig
assert(result < slice.len);
assert(slice[result] == value);
```

## What the test asserts

- Last occurrence wins over earlier matches
- Repeated scalar returns the final index
- Missing scalar returns null
- Empty slice returns null
- Path-like string finds the last dot
