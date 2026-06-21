# Pass 9915 · mem.replaceOwned — allocation matches replacement walk

**Witnesses:** 88 programs (grew from 87)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.033412`

## What this pass covers

**`std.mem.replaceOwned`** — allocate output via `replacementSize`, fill with `replace`. Completes the replace trio with `replacementSize` (9916) and `replace` (9917).

## Rye std surface

**`std.mem.replaceOwned`**

```zig
pub fn replaceOwned(comptime T: type, allocator: Allocator, input: []const T, needle: []const T, replacement: []const T) Allocator.Error![]T
```

## Width notes

**`std.mem.replaceOwned`** — Public signature inherits Zig `usize` for slice lengths via `replacementSize` / `replace`. Named verify bound `max_replace_owned_input: u32 = 64` at the slice seam.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]const T`, alloc length) | `usize` — Zig seam |
| Named verify bound | `u32` + `@as(usize, …)` |
| Allocator length | from `replacementSize` (9916) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `replaceOwned` — `u32` verify bound; `output.len == expected_len` | done |
| `rye/tests/mem_replace_owned_test.rye` | `page_allocator`; no authored struct `usize` | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9916_mem_replacement_size.md` | sibling; sizes allocation | unchanged |
| `strengthening-compiler/9917_mem_replace.md` | sibling; fills buffer | unchanged |
| `992_strengthening_width_crosswalk.md` | row 9915 via enricher | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.replaceOwned` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

`output.len == replacementSize(...)`. When `input.len <= 64`, independent verify walk confirms each emitted span in the allocated slice.

## What the test asserts

- `base` → `Zig` replacement with length 29
- ` code` → empty in zen string
