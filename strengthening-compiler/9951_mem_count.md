# Pass 9951 · mem.count — non-overlapping needle tally stays in bounds

**Witnesses:** 52 programs (grew from 51)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.184712`

## What this pass covers

**`std.mem.count`** and **`countScalar`** — tally non-overlapping needle occurrences (or scalar elements). Complements `findPos` (9971) and `contains` patterns in string builtins.

## Postconditions

**count** — each match and final state:

```zig
assert(idx >= i);
assert(idx + needle.len <= haystack.len);
assert(i <= haystack.len);
assert(found <= haystack.len);
```

**countScalar**:

```zig
assert(found <= list.len);
```

## What the test asserts

- Empty haystack, single and double scalar hits
- Multi-byte needle non-overlap (`foo`, `ff`, `abc`)
- `countScalar` on spaced `abc` string
