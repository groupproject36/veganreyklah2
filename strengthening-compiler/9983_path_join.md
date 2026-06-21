# Pass 9983 · path.join — buffer fully filled, empty components documented

**Corpus:** 21 programs (grew from 20)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.144812`

## What this pass covers

**`std.fs.path.join`** (via `joinSepMaybeZ`) — composes path components with the native separator. Pond policy (`10009`) and future Rishi path helpers lean on this.

At `joinSepMaybeZ` return:

```zig
assert(buf_index == buf.len - @as(usize, @intFromBool(zero)));
```

At `join` cold wrapper — empty components are valid input (skipped, same as `formatJoin`):

```zig
for (paths) |p| std.debug.maybe(p.len == 0);
```

## Rye std surface

**`std.fs.path.join`**

```zig
pub fn join(allocator: Allocator, paths: []const []const u8) ![]u8
```

## Width notes

**`std.fs.path.join`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## What the test asserts

- Multi-component join matches expected POSIX-style path
- Empty middle component skipped
- Adjacent separators merged (`base/` + `file`)
- Single component, zero components, all-empty components
- Parity holds against baseline std

## Pond note

Full “stay within declared root” enforcement belongs in Pond policy code, not in `path.join` itself — join stays parity-identical while stating its buffer invariant.
