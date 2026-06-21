# Pass 9938 · endsWith — suffix verdict agrees with eql

**Witnesses:** 65 programs (grew from 64)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.201912`

## What this pass covers

**`std.mem.endsWith`** — suffix test on slices. The `rye` CLI checks `.rye` suffixes; pairs with `startsWith` (9939) on the Aurora metal lane (`995`).

## Rye std surface

**`std.mem.endsWith`**

```zig
pub fn endsWith(comptime T: type, haystack: []const T, needle: []const T) bool
```

## Width notes

**`std.mem.endsWith`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Postconditions

- `false` when `needle.len > haystack.len` ⇒ length ordering stated
- `true` ⇒ `needle.len <= haystack.len`
- `false` otherwise ⇒ empty needle or suffix `eql` fails

## What the test asserts

- Normal suffix match and mismatch
- Empty needle (always true)
- Needle longer than haystack
- Equal-length exact match
