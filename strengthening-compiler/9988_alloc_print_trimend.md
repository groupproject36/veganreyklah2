# Pass 9988 · allocPrint and trimEnd — the path conversion and parsing layer

**Witnesses:** 16 programs (grew from 15)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260619.225712`

## What this pass covers

Two `std` functions our recent code depends on, now exercised in the parity witnesses:

1. **`std.fmt.allocPrint`** — allocates a formatted, sentinel-terminated string. Used in Rishi's file I/O builtins (`doReadFile`, `doListDir`, `doWriteFile`) to convert Rishi string values (non-sentinel `[]const u8`) to OS-boundary-safe `[:0]u8` paths. Also used in Mantra's `Store` methods for path construction.

2. **`std.mem.trimEnd`** — removes trailing characters from a slice. Used in Rishi's arithmetic parser (`findLastArithAdd`) to detect binary operators by checking that the trimmed left side ends with a value token rather than another operator.

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

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/fmt.zig` | `allocPrint` — Phase 4 `usize` seam policy applied | done |
| `rye/lib/std/mem.zig` | `trimEnd` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/alloc_print_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9988_alloc_print_trimend.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9988 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.fmt.allocPrint` — [`rye/lib/std/fmt.zig`](../rye/lib/std/fmt.zig)
- [x] `std.mem.trimEnd` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## What the test asserts

- `allocPrint` produces output matching the format exactly (string interpolation, integer formatting, identity formatting)
- Output length matches expected values
- `trimEnd` removes only trailing matches, leaves leading characters untouched
- `trimEnd` on an empty string returns empty
- `trimEnd` result length is always <= input length

## Design notes

The test uses `page_allocator` (not `init.garden`) so it compiles identically against both the baseline and Rye's strengthened std — the same pattern `mantra_weave_test` and `tally_gardens_test` keep.
