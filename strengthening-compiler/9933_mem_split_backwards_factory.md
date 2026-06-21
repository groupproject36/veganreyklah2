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

## Postconditions

On return from each factory:

- `index == buffer.len`
- `rest().len == buffer.len` (full buffer visible before first `next`)

## What the test asserts

- Scalar, any, and sequence delimiters at creation
- Empty buffer: `rest` is zero-length; `first` yields empty field
