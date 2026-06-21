# Pass 9928 · mem.span — sentinel slice length matches len

**Witnesses:** 75 programs (grew from 74)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.013412`

## What this pass covers

**`std.mem.span`** — sentinel-terminated pointer to slice. Pairs with `len` (9942) and `sliceTo` (9945).

## Rye std surface

**`std.mem.span`**

```zig
pub fn span(ptr: anytype) Span(@TypeOf(ptr))
```

## Width notes

**`std.mem.span`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `span` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/mem_span_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9928_mem_span.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9928 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.span` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

Returned slice length equals `len(ptr)`. When the result is sentinel-terminated, the element at that index is the sentinel.

## What the test asserts

- Custom sentinel on `[:3]u16` pointer
- `[*:0]const u8` C string with embedded NUL
- String literal span
- Optional null pointer returns null
