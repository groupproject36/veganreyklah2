# Pass 9942 · mem.len — sentinel length points at terminator

**Witnesses:** 61 programs (grew from 60)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.195112`

## What this pass covers

**`std.mem.len`** — length of sentinel-terminated many-item and `[*c]` pointers. Pairs with `sliceTo` (9945) and `findSentinel` (9952).

## Postconditions

On return, the byte/element at the returned index is the sentinel (`0` for `[*c]`).

## What the test asserts

- Custom sentinel on `[:4]u16` pointer
- `[*:0]const u8` C string with embedded NUL
- Empty C string
- String literal length
