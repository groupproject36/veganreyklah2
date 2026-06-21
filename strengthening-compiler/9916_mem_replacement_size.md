# Pass 9916 · mem.replacementSize — buffer size matches replacement count

**Witnesses:** 87 programs (grew from 86)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.032712`

## What this pass covers

**`std.mem.replacementSize`** — calculate output buffer length for `replace`. Pairs with `mem.replace` (9917) and `startsWith` (9939).

## Rye std surface

**`std.mem.replacementSize`**

```zig
pub fn replacementSize(comptime T: type, input: []const T, needle: []const T, replacement: []const T) usize
```

## Width notes

**`std.mem.replacementSize`** — Public signature inherits Zig `usize` for slice lengths and return value — keep at the inherited seam per `992` Phase 4. Named verify bound `max_replacement_size_input: u32 = 64` with comparison at the slice seam.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, return `usize`) | `usize` — Zig seam |
| Named verify bound (`max_replacement_size_input`) | `u32` + `@as(usize, …)` |
| Replacement-count delta math | `isize` bridge for `replacement.len - needle.len` |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `replacementSize` — `u32` verify bound; `isize` delta; public `usize` unchanged | done |
| `rye/tests/mem_replacement_size_test.rye` | witness uses std test vectors only; no authored `usize` fields | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9917_mem_replace.md` | sibling pass; calls `replacementSize` in precondition | unchanged |
| `992_strengthening_width_crosswalk.md` | row 9916 added via enricher | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.replacementSize` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

Precondition: `needle.len > 0`. After walk, `i == input.len`. When `input.len <= 64`, `size == input.len + reps * (replacement.len - needle.len)` via `isize` delta.

## What the test asserts

- Known sizes from std tests (`base`→`Zig`, empty `code`, empty input)
- Adjacent replacements (`abbba`, `\\n\\n`)
