# Pass 9943 · copyForwards — copied prefix matches source

**Witnesses:** 60 programs (grew from 59)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.194512`

## What this pass covers

**`std.mem.copyForwards`** — copy from the start for overlapping destinations where `dest.ptr <= source.ptr`. Pairs with `copyBackwards` (9944); Mantra weave logic depends on the forward direction (9993).

## Rye std surface

**`std.mem.copyForwards`**

```zig
pub fn copyForwards(comptime T: type, dest: []T, source: []const T) void
```

## Width notes

**`std.mem.copyForwards`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `copyForwards` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/mem_copy_forwards_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9943_mem_copy_forwards.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9943 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.copyForwards` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postcondition

When source and destination do not overlap:

```zig
assert(eql(T, dest[0..source.len], source));
```

Overlapping copies skip the assert — aliased memory may mutate `source` during the forward walk.

## What the test asserts

- Non-overlapping prefix copy into a larger buffer
- Overlapping copy when destination starts before source (`memmove` semantics)
- Empty source is a no-op
