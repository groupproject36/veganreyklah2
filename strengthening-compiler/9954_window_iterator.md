# Pass 9954 · WindowIterator — sliding windows stay in-range

**Corpus:** 49 programs (grew from 48)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.181512`

## What this pass covers

**`WindowIterator.next`** and **`reset`** (via `mem.window`) — fixed-size sliding windows over a buffer. Used in `debug` hex dumps, `base64`, and `Io.Writer` chunking.

## Rye std surface

**`std.mem.window`**

```zig
pub fn window(comptime T: type, buffer: []const T, size: usize, advance: usize) WindowIterator(T)
```

## Width notes

**`std.mem.window`** — Public signature inherits Zig `usize` for slice lengths and indices — keep at the inherited seam per `992` Phase 4. Narrow to `u32`/`u64` only for named bounds inside the body (`max_*_check`, loop counters) with `assert` before `@intCast`.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `window` — inherited `usize` seam; assertions only | done |
| `rye/tests/window_iterator_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9954_window_iterator.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9954 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.window` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

**next**:

```zig
assert(start <= end);
assert(end <= self.buffer.len);
```

**reset**:

```zig
assert(self.index.? == 0);
```

## What the test asserts

- Non-overlapping chunks (size == advance)
- Overlapping slide (advance 1)
- Empty buffer returns null
- `reset()` replays first window
