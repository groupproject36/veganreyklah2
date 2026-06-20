# Pass 9950 · containsAtLeast — threshold tally agrees with scan bounds

**Witnesses:** 53 programs (grew from 52)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.185712`

## What this pass covers

**`std.mem.containsAtLeast`** and **`containsAtLeastScalar2`** — true when a needle or scalar appears at least N times (non-overlapping for needles). Pairs with `mem.count` (9951).

## Postconditions

**containsAtLeast** — same in-loop bounds as count; on return:

- `true` ⇒ `found >= expected_count`
- `false` ⇒ `found < expected_count`

**containsAtLeastScalar2**:

- `true` ⇒ `found >= minimum` and `found <= list.len`
- `false` ⇒ `found < minimum` and `found <= list.len`

## What the test asserts

- Scalar and multi-byte thresholds, met and unmet
- Non-overlapping `radar` case
- `containsAtLeastScalar2` on `adadda`
