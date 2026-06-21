# Pass 9985 · writeStreamingAll — every byte consumed

**Corpus:** 19 programs (grew from 18)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.143912`

## What this pass covers

**`std.Io.File.writeStreamingAll`** — loops `writeStreaming` until the full slice is sent. Rishi's `say`, Brushstroke stdout lines, and Rishi value printing all call it on every output.

Postcondition after the loop:

```zig
assert(index == bytes.len);
```

## Rye std surface

**`std.Io.File.writeStreamingAll`**

```zig
pub fn writeStreamingAll(file: File, io: Io, bytes: []const u8) Writer.Error!void
```

## Width notes

**`std.Io.File.writeStreamingAll`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/Io/File.zig` | `File.writeStreamingAll` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/write_streaming_all_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9985_write_streaming_all.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9985 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.Io.File.writeStreamingAll` — [`rye/lib/std/Io/File.zig`](../rye/lib/std/Io/File.zig)

## What the test asserts

- Non-empty write round-trips through a temp file via `readFile`
- Empty write completes without error (index stays 0)
- Parity holds against baseline std

## Call graph note

`writeStreamingAll` → `writeStreaming` (hot path). The invariant lands at the cold wrapper so the streaming syscall loop stays lean.
