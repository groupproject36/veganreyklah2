# Pass 9936 · Keccak sponge @memcpy — slice bounds at absorb and squeeze

**Witnesses:** 67 programs (grew from 66)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.203912`

## What this pass covers

**`keccak_p.State.absorb` and `squeeze`** — `@memcpy` slice bounds beside existing `offset <= rate` discipline. Every SHA3 hash on Aurora's metal path walks these copies (`9997`–`9998`).

## Rye std surface

**`std.crypto.keccak`** — see `rye/lib/std` (signature not auto-located).

## Width notes

**`std.crypto.keccak`** — Authored module or iterator family — width migration lives in Tier A (`992`); std iterator indices remain `usize` until wrapped at our API.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/crypto/keccak_p.zig` | `keccak` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/keccak_sponge_memcpy_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9936_keccak_sponge_memcpy.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9936 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.crypto.keccak` — [`rye/lib/std/crypto/keccak_p.zig`](../rye/lib/std/crypto/keccak_p.zig)

## Postconditions

Before each `@memcpy` in absorb and squeeze partial-block paths:

- Copy length fits source and destination slices
- `self.offset + left <= rate` on absorb into the sponge buffer

## What the test asserts

- SHA3-256 one-shot vs split `update` across a 136-byte block boundary
- Split `update` + `squeeze` exercises squeeze partial path
