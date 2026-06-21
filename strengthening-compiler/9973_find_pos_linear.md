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
