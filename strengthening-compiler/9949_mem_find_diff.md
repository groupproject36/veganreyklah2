# Pass 9949 · findDiff — first inequality agrees with equality

**Witnesses:** 54 programs (grew from 53)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.191212`

## What this pass covers

**`std.mem.findDiff`** — index of first differing element, or null when slices are equal. Complements `mem.eql` (9996) and `mem.order` (9953).

## Postconditions

On every return path:

- `null` ⇒ `eql(a, b)`
- `Some(idx)` ⇒ `idx == @min(a.len, b.len)` when lengths differ, else `a[idx] != b[idx]` with `idx < shortest`

## What the test asserts

- Equal slices, length mismatch at common prefix end, mid-string diff
- Shared-pointer sub-slice vs full slice
