# Pass 9969 · SplitIterator.peek — lookahead stays within the buffer

**Corpus:** 34 programs (grew from 33)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.165112`

## What this pass covers

**`SplitIterator.peek`** (via `splitScalar`, `splitAny`, `splitSequence`) — returns the next field without advancing. Rishi peeks while splitting lines and fields; `next()` was strengthened in 9993.

## Rye std surface

**`std.mem.split`** — see `rye/lib/std` (signature not auto-located).

## Width notes

**`std.mem.split`** — Authored module or iterator family — width migration lives in Tier A (`992`); std iterator indices remain `usize` until wrapped at our API.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `split` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/split_peek_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9969_split_peek.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9969 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.split` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postcondition

```zig
assert(start <= end);
assert(end <= self.buffer.len);
```

Same contract as `next()`, stated at peek so lookahead cannot name bytes outside the buffer.

## What the test asserts

- first + peek + next agree on the same field
- Empty field between delimiters visible via peek
- Final peek is null when exhausted
