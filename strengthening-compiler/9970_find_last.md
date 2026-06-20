# Pass 9970 · findLast — backward search entry states the fit contract

**Corpus:** 33 programs (grew from 32)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.164812`

## What this pass covers

**`std.mem.findLast`** (`lastIndexOf`) — unified backward sub-slice search. Delegates to `findLastLinear` (9972) or reverse Boyer-Moore-Horspool; complements `find` / `findPos` (9971).

## Postcondition

On reverse BMH match:

```zig
assert(result + needle.len <= haystack.len);
```

`findLastLinear` path already strengthened (9972). Empty needle returns `haystack.len` per std semantics.

## What the test asserts

- Last repeated needle wins
- Single-char last match
- Not found
- Empty needle at haystack.len
- Long haystack exercises reverse BMH path
