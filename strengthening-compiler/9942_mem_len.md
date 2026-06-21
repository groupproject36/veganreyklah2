# Pass 9942 · mem.len — sentinel length points at terminator

**Witnesses:** 61 programs (grew from 60)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.195112`

## What this pass covers

**`std.mem.len`** — length of sentinel-terminated many-item and `[*c]` pointers. Pairs with `sliceTo` (9945) and `findSentinel` (9952).

## Rye std surface

**`std.mem.len`**

```zig
pub fn len(value: anytype) usize
```

## Width notes

**`std.mem.len`** — Public signature inherits Zig `usize` for slice lengths and indices — keep at the inherited seam per `992` Phase 4. Narrow to `u32`/`u64` only for named bounds inside the body (`max_*_check`, loop counters) with `assert` before `@intCast`.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Postconditions

On return, the byte/element at the returned index is the sentinel (`0` for `[*c]`).

## What the test asserts

- Custom sentinel on `[:4]u16` pointer
- `[*:0]const u8` C string with embedded NUL
- Empty C string
- String literal length
