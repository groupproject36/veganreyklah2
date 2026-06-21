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

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `tokenize` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/tokenize_peek_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9957_tokenize_peek.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9957 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.tokenize` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

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
