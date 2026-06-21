# Pass 9928 · mem.span — sentinel slice length matches len

**Witnesses:** 75 programs (grew from 74)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.013412`

## What this pass covers

**`std.mem.span`** — sentinel-terminated pointer to slice. Pairs with `len` (9942) and `sliceTo` (9945).

## Rye std surface

**`std.mem.span`**

```zig
pub fn span(ptr: anytype) Span(@TypeOf(ptr))
```

## Width notes

**`std.mem.span`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Postconditions

Returned slice length equals `len(ptr)`. When the result is sentinel-terminated, the element at that index is the sentinel.

## What the test asserts

- Custom sentinel on `[:3]u16` pointer
- `[*:0]const u8` C string with embedded NUL
- String literal span
- Optional null pointer returns null
