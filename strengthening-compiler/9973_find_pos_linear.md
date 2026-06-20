# Pass 9973 · findPosLinear — offset needle search stays in-range

**Corpus:** 30 programs (grew from 29)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.163512`

## What this pass covers

**`std.mem.findPosLinear`** (`indexOfPosLinear`) — linear forward search for a sub-slice from `start_index`. `findPos` delegates here on small inputs; complements `find` (9993) and the scalar search trio (9974–9975, 9996).

## Postcondition

On match:

```zig
assert(i + needle.len <= haystack.len);
assert(i >= start_index);
```

## What the test asserts

- First match from zero
- Next match from offset
- No match when offset is past end
- Single-byte and multi-byte needles
- Second occurrence found when search starts after first
