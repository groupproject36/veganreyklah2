# Pass 9933 · mem split backwards factories — cursor starts at buffer end

**Witnesses:** 70 programs (grew from 69)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.205912`

## What this pass covers

**`splitBackwardsScalar`, `splitBackwardsAny`, `splitBackwardsSequence`** — factory postconditions beside strengthened `SplitBackwardsIterator` (`9962`) and forward factories (`9934`).

## Rye std surface

**`std.mem.split_backwards_factory`** — see `rye/lib/std` (signature not auto-located).

## Width notes

**`std.mem.split_backwards_factory`** — Authored module or iterator family — width migration lives in Tier A (`992`); std iterator indices remain `usize` until wrapped at our API.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `split_backwards_factory` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/mem_split_backwards_factory_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9933_mem_split_backwards_factory.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9933 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.split_backwards_factory` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

On return from each factory:

- `index == buffer.len`
- `rest().len == buffer.len` (full buffer visible before first `next`)

## What the test asserts

- Scalar, any, and sequence delimiters at creation
- Empty buffer: `rest` is zero-length; `first` yields empty field
