# Pass 9929 · crypto.secureZero — volatile slice wiped to zero

**Witnesses:** 74 programs (grew from 73)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.013112`

## What this pass covers

**`std.crypto.secureZero`** — volatile `@memset` that compilers cannot elide. Every AEAD decrypt failure path and bcrypt cleanup walks this wipe.

## Rye std surface

**`std.crypto.secureZero`**

```zig
pub fn secureZero(self: *Self) void
```

## Width notes

**`std.crypto.secureZero`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Postconditions

After `@memset`:

- Every byte of `s.len * @sizeOf(T)` is zero (read back through volatile `u8` — works for struct state like `Poly1305`)

## What the test asserts

- `u8` and `u32` buffers zeroed completely
- Empty slice is a no-op
