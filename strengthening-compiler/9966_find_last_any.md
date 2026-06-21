# Pass 9966 · findLastAny — backward any-delimiter search stays in-range

**Corpus:** 37 programs (grew from 36)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.170312`

## What this pass covers

**`std.mem.findLastAny`** (`lastIndexOfAny`) — backward search for any of a set of scalars. Backs `SplitBackwardsIterator` with `.any` delimiters; pairs with `findAnyPos` (9967).

## Rye std surface

**`std.mem.findLastAny`**

```zig
pub fn findLastAny(comptime T: type, slice: []const T, values: []const T) ?usize
```

## Width notes

**`std.mem.findLastAny`** — Public signature inherits Zig `usize` for slice lengths and indices — keep at the inherited seam per `992` Phase 4. Narrow to `u32`/`u64` only for named bounds inside the body (`max_*_check`, loop counters) with `assert` before `@intCast`.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `findLastAny` — inherited `usize` seam; assertions only | done |
| `rye/tests/find_last_any_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9966_find_last_any.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9966 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.findLastAny` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postcondition

On match:

```zig
assert(i < slice.len);
assert(slice[i] == value);
```

## What the test asserts

- Last match in mixed string (std upstream case)
- Last delimiter in path-like string
- Repeated scalar returns final index
- Absent set returns null
