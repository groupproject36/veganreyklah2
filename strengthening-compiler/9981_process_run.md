# Pass 9981 · process.run — the process boundary Rishi orchestrates through

**Corpus:** 22 programs (grew from 21)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.151812`

## What this pass covers

**`std.process.run`** — spawns a child, collects stdout and stderr, waits for exit. Rishi's `run` builtin, `tools/parity.rish`, and `hosted_wire demo` all depend on it.

## Rye std surface

**`std.process.run`**

```zig
pub fn run(gpa: Allocator, io: Io, options: RunOptions) RunError!RunResult
```

## Width notes

**`std.process.run`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/process.zig` | `run` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/process_run_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9981_process_run.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9981 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.process.run` — [`rye/lib/std/process.zig`](../rye/lib/std/process.zig)

## Postconditions

**Entry** (`process.zig`):

```zig
assert(options.argv.len > 0);
```

**Return** — after streams are owned:

```zig
if (options.stdout_limit.toInt()) |limit| {
    assert(stdout_slice.len <= limit);
}
if (options.stderr_limit.toInt()) |limit| {
    assert(stderr_slice.len <= limit);
}
```

## What the test asserts

- `true` exits 0 with empty stdout and stderr
- `echo` captures stdout and returns exit code 0
- `.limited(32)` on stdout holds for a short echo (`bounded.stdout.len <= 32`)

## Call graph note

`process.run` → `spawn` + `MultiReader` + `wait`. Invariants land at the cold wrapper; the fill loop already enforces limits during collection — the return assertions document what success means.
