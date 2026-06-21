# Pass 9957 · TokenIterator.peek and rest — token slices stay in-range

**Corpus:** 46 programs (grew from 45)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.175712`

## What this pass covers

**`TokenIterator.peek`** and **`rest`** (via `tokenizeScalar`, `tokenizeAny`, `tokenizeSequence`) — skip delimiter runs, return non-empty tokens. Pairs with `SplitIterator.peek`/`rest` (9969, 9968).

## Rye std surface

**`std.mem.tokenize`** — see `rye/lib/std` (signature not auto-located).

## Width notes

**`std.mem.tokenize`** — Authored module or iterator family — width migration lives in Tier A (`992`); std iterator indices remain `usize` until wrapped at our API.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

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
