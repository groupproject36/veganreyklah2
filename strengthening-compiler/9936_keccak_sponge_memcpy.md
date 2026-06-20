# Pass 9936 · Keccak sponge @memcpy — slice bounds at absorb and squeeze

**Witnesses:** 67 programs (grew from 66)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.203912`

## What this pass covers

**`keccak_p.State.absorb` and `squeeze`** — `@memcpy` slice bounds beside existing `offset <= rate` discipline. Every SHA3 hash on Aurora's metal path walks these copies (`9997`–`9998`).

## Postconditions

Before each `@memcpy` in absorb and squeeze partial-block paths:

- Copy length fits source and destination slices
- `self.offset + left <= rate` on absorb into the sponge buffer

## What the test asserts

- SHA3-256 one-shot vs split `update` across a 136-byte block boundary
- Split `update` + `squeeze` exercises squeeze partial path
