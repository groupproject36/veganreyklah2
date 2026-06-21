# Pass 9986 · bufPrint — formatted output stays in the caller buffer

**Corpus:** 18 programs (grew from 17)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.143312`

## What this pass covers

**`std.fmt.bufPrint`** — formats into a caller-owned `[]u8` without allocation. Rishi's value printer, Mantra's weave headers, Skate's selftest line, and rye's multi-file bridge error messages all use it for short, bounded output.

Postcondition at the cold wrapper:

```zig
const result = w.buffered();
assert(result.len <= buf.len);
return result;
```

## Rye std surface

**`std.fmt.bufPrint`**

```zig
pub fn bufPrint(buf: []u8, comptime fmt: []const u8, args: anytype) BufPrintError![]u8
```

## Width notes

**`std.fmt.bufPrint`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## What the test asserts

- String interpolation matches expected text
- Integer formatting matches expected text
- Empty format returns length 0
- Single-character format returns length 1 within the buffer
- Result length is always `<=` buffer length (the strengthened postcondition)

## Call graph note

`bufPrint` → `Writer.fixed` → `Writer.print` → `Writer.buffered`. The invariant lands at `bufPrint` so the fixed-buffer writer path stays documented without touching the hot `print` implementation.
