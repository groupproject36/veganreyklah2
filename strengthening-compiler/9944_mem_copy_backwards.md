# Pass 9944 · copyBackwards — copied prefix matches source

**Witnesses:** 59 programs (grew from 58)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.194012`

## What this pass covers

**`std.mem.copyBackwards`** — copy from the end for overlapping destinations where `dest.ptr >= source.ptr`. Pairs with `copyForwards` (9993); Mantra weave logic uses the forward direction; backward copy completes the deprecated copy pair.

## Postcondition

When source and destination do not overlap:

```zig
assert(eql(T, dest[0..source.len], source));
```

Overlapping copies skip the assert — source bytes may be read through aliased memory during the backward walk.

## What the test asserts

- Non-overlapping tail copy into a larger buffer
- Overlapping copy when destination starts after source (`memmove` semantics)
- Empty source is a no-op
