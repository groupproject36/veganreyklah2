# Pass 9928 · mem.span — sentinel slice length matches len

**Witnesses:** 75 programs (grew from 74)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.013412`

## What this pass covers

**`std.mem.span`** — sentinel-terminated pointer to slice. Pairs with `len` (9942) and `sliceTo` (9945).

## Postconditions

Returned slice length equals `len(ptr)`. When the result is sentinel-terminated, the element at that index is the sentinel.

## What the test asserts

- Custom sentinel on `[:3]u16` pointer
- `[*:0]const u8` C string with embedded NUL
- String literal span
- Optional null pointer returns null
