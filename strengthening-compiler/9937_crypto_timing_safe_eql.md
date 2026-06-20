# Pass 9937 · timing_safe.eql — constant-time verdict matches xor accumulator

**Witnesses:** 66 programs (grew from 65)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.203612`

## What this pass covers

**`std.crypto.timing_safe.eql`** — constant-time equality for short secrets (AEAD tags, MACs). First Aurora metal-lane surface on the main track (`995`); ChaCha20-Poly1305 decrypt uses it internally.

## Postconditions

On return, `true` iff the xor accumulator is zero (array and vector paths).

## What the test asserts

- Equal and unequal 32-byte arrays
- 16-byte tag-like arrays with single-bit flip
