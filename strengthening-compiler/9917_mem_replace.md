# Pass 9917 · mem.replace — output length and content verified

**Witnesses:** 86 programs (grew from 85)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.031512`

## What this pass covers

**`std.mem.replace`** — replace every needle occurrence in input, writing to a caller buffer. Pairs with `startsWith` (9939) and `replacementSize`.

## Postconditions

Precondition: `replacementSize(...) <= output.len`. After the walk, write index equals `replacementSize`. When `input.len <= 64` and output fits in 128 elements, independent verify loop confirms each emitted span.

## What the test asserts

- Single replacement (`base` → `Zig`)
- Adjacent replacements (`b` → `cd` in `abbba`)
- Empty input yields zero replacements
