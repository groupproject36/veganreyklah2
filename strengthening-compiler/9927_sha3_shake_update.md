# Pass 9927 · SHA3 ShakeLike update — sponge cursor within rate

**Witnesses:** 76 programs (grew from 75)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.015112`

## What this pass covers

**`ShakeLike.update` in `sha3.zig`** — sponge cursor bounds after every absorb on the XOF path. Pairs with Keccak `update` (9994 family), `ShakeLike.squeeze` (9935), and `keccak_p` (9936).

## Postconditions

After absorb: `st.offset <= block_length`; `maybe(st.offset == block_length)`; buffered `offset <= buf.len`.

## What the test asserts

- Three-chunk absorb then squeeze matches `Shake128.hash` one-shot
- Input length crosses partial and full block boundaries
