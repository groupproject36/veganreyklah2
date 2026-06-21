# Pass 9932 · mem tokenize factories — cursor starts at buffer front

**Witnesses:** 71 programs (grew from 70)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.210412`

## What this pass covers

**`tokenizeScalar`, `tokenizeAny`, `tokenizeSequence`** — factory postconditions beside strengthened `TokenIterator` (`9956`–`9957`) and split factories (`9934`).

## Rye std surface

**`std.mem.tokenize_factory`** — see `rye/lib/std` (signature not auto-located).

## Width notes

**`std.mem.tokenize_factory`** — Authored module or iterator family — width migration lives in Tier A (`992`); std iterator indices remain `usize` until wrapped at our API.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `tokenize_factory` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/mem_tokenize_factory_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9932_mem_tokenize_factory.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9932 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.tokenize_factory` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

On return from each factory:

- `index == 0`
- `index <= buffer.len`

Unlike split factories, `rest()` skips leading delimiters — not asserted at creation.

## What the test asserts

- Scalar, any, and sequence delimiters: `peek` on first token, `rest` from first token start
- Empty buffer and delimiter-only buffer yield null `peek`
