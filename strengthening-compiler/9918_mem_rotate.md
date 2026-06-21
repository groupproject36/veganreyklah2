# Pass 9918 · mem.rotate — left-rotate matches snapshot

**Witnesses:** 85 programs (grew from 84)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.030912`

## What this pass covers

**`std.mem.rotate`** — in-place left rotation via three `reverse` calls. Pairs with `mem.reverse` (9921) and `mem.swap` (9919).

## Postconditions

Precondition: `amount <= items.len`. When `items.len <= 64` and `items.len > 0`, each index holds the original at `(j + amount) % len` (`eql(u8, asBytes(...))`).

## What the test asserts

- Five-element `i32` rotate by 2
- Four-element `u8` rotate by 1
- Rotate by 0 leaves order unchanged
