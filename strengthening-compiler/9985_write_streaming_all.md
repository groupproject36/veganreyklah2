# Pass 9985 · writeStreamingAll — every byte consumed

**Corpus:** 19 programs (grew from 18)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.143912`

## What this pass covers

**`std.Io.File.writeStreamingAll`** — loops `writeStreaming` until the full slice is sent. Rishi's `say`, Brushstroke stdout lines, and Rishi value printing all call it on every output.

Postcondition after the loop:

```zig
assert(index == bytes.len);
```

## Rye std surface

**`std.Io.File.writeStreamingAll`**

```zig
pub fn writeStreamingAll(file: File, io: Io, bytes: []const u8) Writer.Error!void
```

## Width notes

**`std.Io.File.writeStreamingAll`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## What the test asserts

- Non-empty write round-trips through a temp file via `readFile`
- Empty write completes without error (index stays 0)
- Parity holds against baseline std

## Call graph note

`writeStreamingAll` → `writeStreaming` (hot path). The invariant lands at the cold wrapper so the streaming syscall loop stays lean.
