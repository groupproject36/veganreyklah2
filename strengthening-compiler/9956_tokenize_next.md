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

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `tokenize` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/tokenize_next_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9956_tokenize_next.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9956 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.tokenize` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

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
