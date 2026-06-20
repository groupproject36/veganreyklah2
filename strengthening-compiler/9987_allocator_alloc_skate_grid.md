# Pass 9987 · Allocator.alloc — slice length matches request

**Witnesses:** 17 programs (grew from 16)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.050912`

## What this pass covers

**`std.mem.Allocator.alloc`** (via `allocAdvancedWithRetAddr`) — the allocation path Skate's `Grid.init`, Wayland seeds, and Rishi builtins walk when they need a fresh slice.

Postcondition added at the cold wrapper:

```zig
const result = ptr[0..n];
assert(result.len == n);
return result;
```

## What the tests assert

- `allocator_alloc_test.rye` — `alloc(u8, 16)` returns length 16; `alloc(u32, 4)` returns 4; zero-length alloc returns `len == 0`
- `rye run brushstroke/skate_grid_test.rye` — end-to-end Skate grid through strengthened `alloc` + `copyForwards` (multi-file bridge; outside parity witnesses)

## Brushstroke migration (`050912`)

- `brushstroke/skate_grid.zig` → `skate_grid.rye` with TAME assertions on grid invariants
- `brushstroke/font8x8_data.zig` → `font8x8_data.rye` (glyph data only)
- `putLine` uses `std.mem.copyForwards` (pass 9993) instead of `@memcpy`
- `rye build` now bridges local `@import("*.rye")` dependencies recursively to ephemeral `.zig` files
