# Pass 9982 · allocPrint and trimEnd — postconditions on the formatting and trim layer

**Witnesses:** 21 programs (unchanged — `alloc_print_test` from pass 9988)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.150112`

## What this pass covers

Pass 9988 added `rye/tests/alloc_print_test.rye` to the parity witnesses. This pass lands TAME postconditions in the strengthened `std` so the gate exercises assertions at runtime, not only in the test file.

1. **`std.fmt.allocPrint`** — Rishi path conversion (`doReadFile`, `doListDir`, `doWriteFile`), Mantra path construction.

2. **`std.mem.trimEnd`** — Rishi arithmetic parser (`findLastArithAdd`) and line trimming in the interpreter loop.

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
