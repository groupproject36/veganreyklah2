# Pass 9927 · SHA3 ShakeLike update — sponge cursor within rate

**Witnesses:** 76 programs (grew from 75)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.015112`

## What this pass covers

**`ShakeLike.update` in `sha3.zig`** — sponge cursor bounds after every absorb on the XOF path. Pairs with Keccak `update` (9994 family), `ShakeLike.squeeze` (9935), and `keccak_p` (9936).

## Rye std surface

**`std.crypto.sha3`** — see `rye/lib/std` (signature not auto-located).

## Width notes

**`std.crypto.sha3`** — Authored module or iterator family — width migration lives in Tier A (`992`); std iterator indices remain `usize` until wrapped at our API.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/crypto/sha3.zig` | `sha3` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/sha3_shake_update_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9927_sha3_shake_update.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9927 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.crypto.sha3` — [`rye/lib/std/crypto/sha3.zig`](../rye/lib/std/crypto/sha3.zig)

## Postconditions

After absorb: `st.offset <= block_length`; `maybe(st.offset == block_length)`; buffered `offset <= buf.len`.

## What the test asserts

- Three-chunk absorb then squeeze matches `Shake128.hash` one-shot
- Input length crosses partial and full block boundaries
