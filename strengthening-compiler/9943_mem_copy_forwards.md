# Pass 9943 · copyForwards — copied prefix matches source

**Witnesses:** 60 programs (grew from 59)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.194512`

## What this pass covers

**`std.mem.copyForwards`** — copy from the start for overlapping destinations where `dest.ptr <= source.ptr`. Pairs with `copyBackwards` (9944); Mantra weave logic depends on the forward direction (9993).

## Postcondition

When source and destination do not overlap:

```zig
assert(eql(T, dest[0..source.len], source));
```

Overlapping copies skip the assert — aliased memory may mutate `source` during the forward walk.

## What the test asserts

- Non-overlapping prefix copy into a larger buffer
- Overlapping copy when destination starts before source (`memmove` semantics)
- Empty source is a no-op
