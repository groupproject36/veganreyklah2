# Pass 9956 · TokenIterator.next — token advance stays in-range

**Corpus:** 47 programs (grew from 46)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.180012`

## What this pass covers

**`TokenIterator.next`** (via `tokenizeScalar`, `tokenizeAny`, `tokenizeSequence`) — returns current token and advances. Pairs with `peek`/`rest` (9957).

## Rye std surface

**`std.mem.tokenize`** — see `rye/lib/std` (signature not auto-located).

## Width notes

**`std.mem.tokenize`** — Authored module or iterator family — width migration lives in Tier A (`992`); std iterator indices remain `usize` until wrapped at our API.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

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
