# Pass 9930 · mem.trim — both ends stay within the input

**Witnesses:** 73 programs (grew from 72)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.012812`

## What this pass covers

**`std.mem.trim`** — removes leading and trailing characters. Completes the trim witness family beside `trimStart` (9979) and `trimEnd` (9988); Rishi calls `trim` on every parsed line.

## Rye std surface

**`std.mem.trim`**

```zig
pub fn trim(comptime T: type, slice: []const T, values_to_strip: []const T) []const T
```

## Width notes

**`std.mem.trim`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Postconditions

- `begin <= end` and `end <= slice.len` (existing)
- `result.len <= slice.len`
- `result.len == end - begin`

## What the test asserts

- Both ends stripped, no-op, empty input
- Result length never exceeds input
- Leading-only and trailing-only cases
