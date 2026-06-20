# Pass 9941 · mem.eql — equality verdict agrees with length and difference

**Witnesses:** 62 programs (grew from 61)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.195412`

## What this pass covers

**`std.mem.eql`** — slice equality. Rishi compares names on every line; complements `findDiff` (9949) and `order` (9953). Builds on the `maybe` documentation from 9996 with return-path postconditions.

## Postconditions

**Vector path (`eqlBytes`):**

- `true` ⇒ `a.len == b.len`
- `false` ⇒ `a.len != b.len` or `findDiff(a, b) != null`

**Scalar path:**

- `false` on length mismatch ⇒ `a.len != b.len`
- `true` on empty or shared pointer ⇒ `a.len == b.len`
- `false` on element mismatch ⇒ differing element at that index
- final `true` ⇒ `a.len == b.len`

## What the test asserts

- Equal and unequal strings, length mismatch, empty slices
- Shared-pointer self-compare
- Mid-string inequality on longer inputs (exercises vector path on u8)
