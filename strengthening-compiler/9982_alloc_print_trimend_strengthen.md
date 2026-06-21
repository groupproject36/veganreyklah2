# Pass 9982 · allocPrint and trimEnd — postconditions on the formatting and trim layer

**Witnesses:** 21 programs (unchanged — `alloc_print_test` from pass 9988)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.150112`

## What this pass covers

Pass 9988 added `rye/tests/alloc_print_test.rye` to the parity witnesses. This pass lands TAME postconditions in the strengthened `std` so the gate exercises assertions at runtime, not only in the test file.

1. **`std.fmt.allocPrint`** — Rishi path conversion (`doReadFile`, `doListDir`, `doWriteFile`), Mantra path construction.

2. **`std.mem.trimEnd`** — Rishi arithmetic parser (`findLastArithAdd`) and line trimming in the interpreter loop.

## Rye std surface

**`std.fmt.allocPrint`**

```zig
pub fn allocPrint(gpa: Allocator, comptime fmt: []const u8, args: anytype) Allocator.Error![]u8
```

**`std.mem.trimEnd`**

```zig
pub fn trimEnd(comptime T: type, slice: []const T, values_to_strip: []const T) []const T
```

## Width notes

**`std.fmt.allocPrint`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

**`std.mem.trimEnd`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Postconditions

**allocPrint** (`fmt.zig`):

```zig
const written_len = aw.writer.end;
const result = try aw.toOwnedSlice();
assert(result.len == written_len);
return result;
```

**trimEnd** (`mem.zig`):

```zig
assert(end <= slice.len);
assert(result.len <= slice.len);
```

## Design notes

`allocPrint` captures `writer.end` before `toOwnedSlice` resets the allocating writer. The invariant pairs with `bufPrint`'s `result.len <= buf.len` (pass 9986): fixed-buffer and heap paths both document length discipline at the cold wrapper.

Corpus entry unchanged — parity already runs `alloc_print_test` on both arms via `rye run`.
