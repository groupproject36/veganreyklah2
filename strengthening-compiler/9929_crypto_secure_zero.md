# Pass 9929 · crypto.secureZero — volatile slice wiped to zero

**Witnesses:** 74 programs (grew from 73)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.013112`

## What this pass covers

**`std.crypto.secureZero`** — volatile `@memset` that compilers cannot elide. Every AEAD decrypt failure path and bcrypt cleanup walks this wipe.

## Postconditions

After `@memset`:

- Every byte of `s.len * @sizeOf(T)` is zero (read back through volatile `u8` — works for struct state like `Poly1305`)

## What the test asserts

- `u8` and `u32` buffers zeroed completely
- Empty slice is a no-op
