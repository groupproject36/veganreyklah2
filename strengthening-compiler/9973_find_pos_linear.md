# Pass 9973 · findPosLinear — offset needle search stays in-range

**Corpus:** 30 programs (grew from 29)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.163512`

## What this pass covers

**`std.mem.findPosLinear`** (`indexOfPosLinear`) — linear forward search for a sub-slice from `start_index`. `findPos` delegates here on small inputs; complements `find` (9993) and the scalar search trio (9974–9975, 9996).

## Rye std surface

**`std.mem.findPosLinear`**

```zig
pub fn findPosLinear(comptime T: type, haystack: []const T, start_index: usize, needle: []const T) ?usize
```

## Width notes

**`std.mem.findPosLinear`** — Public signature inherits Zig `usize` for slice lengths and indices — keep at the inherited seam per `992` Phase 4. Narrow to `u32`/`u64` only for named bounds inside the body (`max_*_check`, loop counters) with `assert` before `@intCast`.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `findPosLinear` — inherited `usize` seam; assertions only | done |
| `rye/tests/find_pos_linear_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9973_find_pos_linear.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9973 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.findPosLinear` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postcondition

On match:

```zig
assert(i + needle.len <= haystack.len);
assert(i >= start_index);
```

## What the test asserts

- First match from zero
- Next match from offset
- No match when offset is past end
- Single-byte and multi-byte needles
- Second occurrence found when search starts after first
