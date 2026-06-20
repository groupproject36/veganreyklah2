# Pass 9958 · cutLast and cutScalarLast — backward split-once stays in-range

**Corpus:** 45 programs (grew from 44)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.175312`

## What this pass covers

**`std.mem.cutLast`** and **`cutScalarLast`** — return before/after slices at the **last** needle occurrence. Pairs with `cut`/`cutScalar` (9959); use `findLast` / `findScalarLast` (9970, 9975).

## Postconditions

Same contract as forward `cut`/`cutScalar` — index in range, parts reassemble haystack.

## What the test asserts

- Absent needle returns null
- Sequence and scalar last-split match upstream cases
