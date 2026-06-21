# Pass 9955 · iterator reset — split and tokenize replay from initial cursor

**Corpus:** 48 programs (grew from 47)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.180712`

## What this pass covers

**`SplitIterator.reset`**, **`SplitBackwardsIterator.reset`**, and **`TokenIterator.reset`** — restore initial cursor position for replay.

## Rye std surface

**`std.mem.Iterator.reset`**

```zig
pub fn reset(self: *Self) void
```

## Width notes

**`std.mem.Iterator.reset`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `reset` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/iterator_reset_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9955_iterator_reset.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9955 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.Iterator.reset` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

| Iterator | After reset |
|----------|-------------|
| Forward split / tokenize | `index == 0` |
| Backward split | `index == buffer.len` |

## What the test asserts

- Forward split `first()` after partial walk + reset
- Backward split `first()` after partial walk + reset
- Tokenize `next()` after partial walk + reset
