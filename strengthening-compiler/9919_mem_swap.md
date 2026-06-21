# Pass 9919 · mem.swap — locations exchange values

**Witnesses:** 84 programs (grew from 83)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.030412`

## What this pass covers

**`std.mem.swap`** — exchange contents of two memory locations. Pairs with `mem.reverse` (9921), which calls `swap` for each mirrored pair.

## Postconditions

After swap at runtime, each pointer holds the other's original bytes (`eql(u8, asBytes(...))`). Comptime swaps skip byte asserts — same rule as the existing comptime branch (undefined layout).

## What the test asserts

- `u8` pair exchanges
- `i32` pair exchanges
- anonymous struct pair exchanges field-wise
