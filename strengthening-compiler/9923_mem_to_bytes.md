# Pass 9923 · mem.toBytes — byte array length matches value size

**Witnesses:** 80 programs (grew from 79)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.023112`

## What this pass covers

**`std.mem.toBytes`** — copies a value's underlying bytes into a fixed array. Pairs with `asBytes` (9925), `bytesToValue`, and the slice view family (9924–9926).

## Postconditions

Returned array length equals `@sizeOf(@TypeOf(value))`.

## What the test asserts

- `u32` yields four bytes matching `asBytes`
- Two-byte struct yields two bytes
