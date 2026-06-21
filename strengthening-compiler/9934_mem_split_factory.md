# Pass 9934 · mem split factories — cursor starts at buffer front

**Witnesses:** 69 programs (grew from 68)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.205212`

## What this pass covers

**`splitScalar`, `splitAny`, `splitSequence`** — factory postconditions beside the strengthened `SplitIterator` methods (`9963`–`9969`, `9993`).

## Rye std surface

**`std.mem.split_factory`** — see `rye/lib/std` (signature not auto-located).

## Width notes

**`std.mem.split_factory`** — Authored module or iterator family — width migration lives in Tier A (`992`); std iterator indices remain `usize` until wrapped at our API.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Postconditions

On return from each factory:

- `index == 0`
- `index <= buffer.len`
- `rest().len == buffer.len` (full buffer visible before first `next`)

## What the test asserts

- Scalar, any, and sequence delimiters at creation
- Empty buffer: `rest` and `peek` are zero-length, not null
