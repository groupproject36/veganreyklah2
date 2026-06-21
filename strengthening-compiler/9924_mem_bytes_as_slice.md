# Pass 9924 · mem.bytesAsSlice — typed slice length matches byte span

**Witnesses:** 79 programs (grew from 78)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.022612`

## What this pass covers

**`std.mem.bytesAsSlice`** — reinterprets `[]u8` as `[]T` preserving pointer attributes. Inverse of `sliceAsBytes` (9926); pairs with `asBytes` (9925).

## Postconditions

Empty bytes or zero-sized `T` returns `len == 0`. Otherwise `result.len * @sizeOf(T) == bytes.len` and `bytes.len % @sizeOf(T) == 0`.

## What the test asserts

- Four bytes as two `u16` values; round-trip via `sliceAsBytes`
- Empty byte slice
- Zero-sized element type
