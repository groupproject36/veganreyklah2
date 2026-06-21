# Pass 9968 · SplitIterator.rest — tail slice stays within the buffer

**Corpus:** 35 programs (grew from 34)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.165512`

## What this pass covers

**`SplitIterator.rest`** — returns the unprocessed tail without advancing. Mantra uses it after `next()` on tab-separated weave rows and newline-split lines.

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
| `rye/tests/split_rest_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9968_split_rest.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9968 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.split` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postcondition

```zig
if (self.index) |idx| assert(idx <= self.buffer.len);
assert(start <= end);
```

## What the test asserts

- rest shrinks as fields are consumed
- rest is empty when iteration completes
- fresh iterator rest is the whole buffer
- Mantra-shaped tab field tail after first column
