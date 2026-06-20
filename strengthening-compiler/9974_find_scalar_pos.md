# Pass 9974 · findScalarPos — offset search stays in-range from start_index

**Corpus:** 29 programs (grew from 28)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.163112`

## What this pass covers

**`std.mem.findScalarPos`** (`indexOfScalarPos`) — scalar search from a start offset. Rishi calls it on every interpolated string (`$`, `}`) and on `let` lines (`=`).

Postcondition lands on the **scalar tail loop** only — vectorized paths stay lean per data-plane economy (9996); the tail loop is where small inputs and remainder scans complete.

## Postcondition

On match in the scalar tail:

```zig
assert(j < slice.len);
assert(slice[j] == value);
assert(j >= start_index);
```

## What the test asserts

- Search from zero finds first match
- Search from middle finds next match
- No match past last occurrence returns null
- start_index at len returns null
- Interpolation-shaped slice finds closing `}`
- `let` line finds `=`
