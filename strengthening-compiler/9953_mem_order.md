# Pass 9953 · mem.order — lexicographic order agrees with equality

**Witnesses:** 50 programs (grew from 49)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.182812`

## What this pass covers

**`std.mem.order`** and **`lessThan`** — lexicographic compare on slices. Backs `SemanticVersion` pre-release ordering and general string sorting.

## Postconditions

**order** — on every return path:

- `.eq` ⇒ `eql(lhs, rhs)`
- `.lt` / `.gt` ⇒ `!eql(lhs, rhs)`

**lessThan** — when true, slices are not equal.

## What the test asserts

- Less, equal, greater by content and by length prefix
- Shared-pointer sub-slice vs full slice
- `lessThan` mirrors `order == .lt`
