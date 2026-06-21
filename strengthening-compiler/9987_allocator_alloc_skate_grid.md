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

## Rye std surface

**`std.mem.Allocator.alloc`**

```zig
pub fn alloc(
            ctx: *anyopaque,
            n: usize,
            alignment: mem.Alignment,
            ret_addr: usize,
        ) ?[*]u8
```

**`std.mem.copyForwards`**

```zig
pub fn copyForwards(comptime T: type, dest: []T, source: []const T) void
```

## Width notes

**`std.mem.Allocator.alloc`** — Public signature inherits Zig `usize` for slice lengths and indices — keep at the inherited seam per `992` Phase 4. Narrow to `u32`/`u64` only for named bounds inside the body (`max_*_check`, loop counters) with `assert` before `@intCast`.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

**`std.mem.copyForwards`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |
