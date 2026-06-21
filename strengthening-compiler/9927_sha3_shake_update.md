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

## Postconditions

After absorb: `st.offset <= block_length`; `maybe(st.offset == block_length)`; buffered `offset <= buf.len`.

## What the test asserts

- Three-chunk absorb then squeeze matches `Shake128.hash` one-shot
- Input length crosses partial and full block boundaries
