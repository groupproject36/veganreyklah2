# Pass 9963 · SplitIterator.first — opening field stays within the buffer

**Corpus:** 40 programs (grew from 39)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.172012`

## What this pass covers

**`SplitIterator.first`** (via `splitScalar`, `splitAny`, `splitSequence`) — returns the first field and advances. Completes the split iterator quartet beside `next` (9993), `peek` (9969), and `rest` (9968).

## Postcondition

After `next()` yields the first field:

```zig
assert(start <= self.buffer.len);
assert(field.len <= self.buffer.len);
assert(start + field.len <= self.buffer.len);
```

Index-based only — `SemanticVersion.parse` calls `first()` at comptime; pointer checks are runtime-only.

## What the test asserts

- Scalar, any, and sequence delimiters
- Leading delimiter yields empty first field
- Single field with no delimiter consumes whole buffer
