# Pass 9984 · readFileAlloc — result respects the stated limit

**Corpus:** 20 programs (grew from 19)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.144112`

## What this pass covers

**`std.Io.Dir.readFileAllocOptions`** (and therefore `readFileAlloc`) — allocates the full file contents. The rye multi-file bridge and Rishi `read-file` lean on this path.

Postcondition at the cold wrapper:

```zig
const max = @intFromEnum(limit);
if (max != std.math.maxInt(usize)) assert(result.len <= max);
return result;
```

`.unlimited` skips the check; every finite limit is enforced at return.

## Rye std surface

**`std.Io.Dir.readFileAllocOptions`**

```zig
pub fn readFileAllocOptions(
    dir: Dir,
    io: Io,
    /// On Windows, should be encoded as [WTF-8](https://wtf-8.codeberg.page/).
    /// On WASI, should be encoded as valid UTF-8.
    /// On other platforms, an opaque sequence of bytes with no particular encoding.
    sub_path: []const u8,
    /// Used to allocate the result.
    gpa: Allocator,
    /// If reached or exceeded, `error.StreamTooLong` is returned instead.
    limit: Io.Limit,
    comptime alignment: std.mem.Alignment,
    comptime sentinel: ?u8,
) ReadFileAllocError!(if (sentinel) |s| [:s]align(alignment.toByteUnits()) u8 else []align(alignment.toByteUnits()) u8)
```

## Width notes

**`std.Io.Dir.readFileAllocOptions`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## What the test asserts

- Round-trip read with `.unlimited` matches written content
- Read with `.limited(n)` where `n` exceeds file size still returns full content
- Empty file read with `.unlimited` returns zero-length slice
- Parity holds against baseline std

## Pair with 9985

9985 strengthened `writeStreamingAll` (stdout/file write path); 9984 strengthens the symmetric read-alloc path our bridge and shell use.
