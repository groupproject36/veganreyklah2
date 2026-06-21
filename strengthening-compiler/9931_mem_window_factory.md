# Pass 9931 · mem.window factory — sliding window starts at buffer front

**Witnesses:** 72 programs (grew from 71)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.212412`

## What this pass covers

**`mem.window`** — factory postconditions beside strengthened `WindowIterator` (`9954`) and sibling factories (`9932`–`9934`).

## Rye std surface

**`std.mem.window_factory`** — see `rye/lib/std` (signature not auto-located).

## Width notes

**`std.mem.window_factory`** — Authored module or iterator family — width migration lives in Tier A (`992`); std iterator indices remain `usize` until wrapped at our API.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `window_factory` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/mem_window_factory_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9931_mem_window_factory.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9931 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.window_factory` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

On return from `window`:

- `size != 0` and `advance != 0` (precondition, unchanged)
- Non-empty buffer: `index == 0` and `index <= buffer.len`
- Empty buffer: `index == null`
- `size` and `advance` match arguments

## What the test asserts

- Chunk and slide modes yield expected first windows at creation
- Empty buffer yields null immediately
- Window larger than buffer returns the whole buffer once
