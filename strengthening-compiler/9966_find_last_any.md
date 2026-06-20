# Pass 9966 · findLastAny — backward any-delimiter search stays in-range

**Corpus:** 37 programs (grew from 36)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.170312`

## What this pass covers

**`std.mem.findLastAny`** (`lastIndexOfAny`) — backward search for any of a set of scalars. Backs `SplitBackwardsIterator` with `.any` delimiters; pairs with `findAnyPos` (9967).

## Postcondition

On match:

```zig
assert(i < slice.len);
assert(slice[i] == value);
```

## What the test asserts

- Last match in mixed string (std upstream case)
- Last delimiter in path-like string
- Repeated scalar returns final index
- Absent set returns null
