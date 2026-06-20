# Pass 9956 · TokenIterator.next — token advance stays in-range

**Corpus:** 47 programs (grew from 46)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.180012`

## What this pass covers

**`TokenIterator.next`** (via `tokenizeScalar`, `tokenizeAny`, `tokenizeSequence`) — returns current token and advances. Pairs with `peek`/`rest` (9957).

## Postcondition

After `peek()` yields a token and index advances:

```zig
assert(token_start <= self.buffer.len);
assert(result.len <= self.buffer.len);
assert(self.index <= self.buffer.len);
assert(token_start + result.len == self.index);
```

## What the test asserts

- Full scalar tokenize walk
- `reset()` replays from start
- `tokenizeAny` and `tokenizeSequence` multi-token paths
