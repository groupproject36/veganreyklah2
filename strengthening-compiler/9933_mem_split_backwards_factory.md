# Pass 9933 · mem split backwards factories — cursor starts at buffer end

**Witnesses:** 70 programs (grew from 69)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.205912`

## What this pass covers

**`splitBackwardsScalar`, `splitBackwardsAny`, `splitBackwardsSequence`** — factory postconditions beside strengthened `SplitBackwardsIterator` (`9962`) and forward factories (`9934`).

## Postconditions

On return from each factory:

- `index == buffer.len`
- `rest().len == buffer.len` (full buffer visible before first `next`)

## What the test asserts

- Scalar, any, and sequence delimiters at creation
- Empty buffer: `rest` is zero-length; `first` yields empty field
