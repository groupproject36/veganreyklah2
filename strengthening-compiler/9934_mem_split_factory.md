# Pass 9934 · mem split factories — cursor starts at buffer front

**Witnesses:** 69 programs (grew from 68)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.205212`

## What this pass covers

**`splitScalar`, `splitAny`, `splitSequence`** — factory postconditions beside the strengthened `SplitIterator` methods (`9963`–`9969`, `9993`).

## Postconditions

On return from each factory:

- `index == 0`
- `index <= buffer.len`
- `rest().len == buffer.len` (full buffer visible before first `next`)

## What the test asserts

- Scalar, any, and sequence delimiters at creation
- Empty buffer: `rest` and `peek` are zero-length, not null
