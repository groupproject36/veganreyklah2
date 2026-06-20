# Pass 9957 · TokenIterator.peek and rest — token slices stay in-range

**Corpus:** 46 programs (grew from 45)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.175712`

## What this pass covers

**`TokenIterator.peek`** and **`rest`** (via `tokenizeScalar`, `tokenizeAny`, `tokenizeSequence`) — skip delimiter runs, return non-empty tokens. Pairs with `SplitIterator.peek`/`rest` (9969, 9968).

## Postconditions

**peek**:

```zig
assert(start <= end);
assert(end <= self.buffer.len);
```

**rest**:

```zig
assert(index <= self.buffer.len);
```

## What the test asserts

- Whitespace tokenize with peek/next agreement
- `rest()` empty after exhaustion
- `tokenizeAny` peek and rest
- Single token with no delimiters
