# 992 · `usize` Width Baseline — inventory before migration

**Stamp:** `20260620.210812`
**Policy:** `context/TAME_STYLE.md` (Rye supplement)
**Charter:** `expanding-prompts/10024_explicit_width_audit.md`
**Status:** Phase 1b underway (`020512`) — `caravan/twin.rye` on `u32`; `caravan/chain` next

---

## Summary

| Tier | Meaning | `usize` occurrences (authored `.rye`) | Action |
|------|---------|----------------------------------------|--------|
| **A — Authored programs** | Seeds, tools, Skate, Rishi, Comlink, Caravan, Mantra, Aurora | **~175** across **22** files | Migrate per Phase 1–3 |
| **B — Witness tests** | `rye/tests/*` | **~15** (mostly boundary sweeps) | Keep at slice edge; narrow locals where easy |
| **C — Inherited std** | `rye/lib/std/**/*.zig` | **thousands** (`mem.zig` alone ~185) | Touch only during strengthening passes |
| **D — Vendor / gratitude** | `vendor/`, `gratitude/` | out of scope | Untouched |

**Contradiction resolved:** TAME supplement previously said “array indices and lengths are `usize`.” Tiger Style and `996_TAME_STYLE.md` say the opposite. **`210812` policy:** `u32` / `u64` in APIs we own; `usize` only at inherited slice boundaries.

---

## Authored `.rye` inventory (Tier A)

| File | `usize` hits | Tier tag | Phase | Notes |
|------|-------------|----------|-------|-------|
| `rishi/src/main.rye` | 37 | interpreter | 3 | line indices, eval stack — prefer `u32` with named max depth |
| `brushstroke/skate_grid.rye` | 29 | display | 1 | `cols`/`rows`/pixel loops → `u32`; cast at `[]u8` stride |
| `comlink/hosted_wire.rye` | 12 | wire | 2 | datagram offsets → `u64` / `u32` per frame spec |
| `caravan/chain.rye` | 12 | supervision | 1 | stage indices bounded by chain depth |
| `caravan/twin.rye` | 0 | supervision | 1 | **Done** `020512` |
| `aurora/src/deciding.rye` | 11 | metal | 2 | MMIO offsets → `u64`; small counters → `u32` |
| `aurora/src/posted.rye` | 11 | metal | 2 | mailbox layout — wire widths |
| `aurora/src/relay.rye` | 8 | metal | 2 | relay buffer walks |
| `caravan/bounded.rye` | 0 | supervision | 1 | **Done** `015712` |
| `tally/gardens.rye` | 0 | memory | 1 | **Done** `211712` |
| `brushstroke/wayland_seed.rye` | 9 | display | 1 | SHM stride / dimension casts |
| `mantra/src/main.rye` | 5 | vcs | 1 | line/weave indices |
| `tally/seed.rye` | 0 | memory | 1 | **Done** `211712` |
| `caravan/seed.rye` | 0 | supervision | 1 | **Done** `014512` |
| `rye/src/main.rye` | 2 | tool | 3 | bridge argv |
| `mantra/src/diff.rye` | 2 | vcs | 1 | LCS table indices |
| `aurora/src/wire.rye` | 1 | metal | 2 | |
| `brushstroke/skate_grid_test.rye` | 4 | test | 1 | follows grid types |
| `rye/tests/tally_gardens_test.rye` | 6 | witness | B | |
| `rye/tests/mantra_weave_test.rye` | 2 | witness | B | |
| `rye/tests/sha3_*_boundary_test.rye` | 2 | witness | B | rate sweep — keep `usize` at `buf[0..n]` edge |

*Counts from ripgrep `usize` token scan, `210812`. Re-run before each phase closes.*

---

## Conversion patterns (reference)

**Struct field (before → after):**

```zig
pos: usize,          // today
pos: u32,            // invariant: pos <= buf.len (and buf.len is bounded at init)
```

**Slice loop (boundary cast):**

```zig
var i: u32 = 0;
while (i < @as(u32, @intCast(buf.len))) : (i += 1) {
    assert(i < buf.len);
    ...
}
```

**Narrowing from slice length:**

```zig
assert(buf.len <= std.math.maxInt(u32));
const n: u32 = @intCast(buf.len);
```

---

## Phase checklist

- [x] **Phase 0** — policy, baseline, living docs (`210812`)
- [x] **Phase 1a** — `tally/seed.rye` + `tally/gardens.rye` (`211712`)
- [ ] **Phase 1b** — `caravan/seed.rye` → `bounded` → `twin` → `chain`
- [ ] **Phase 2** — Aurora + Comlink wire layouts
- [ ] **Phase 3** — Rishi interpreter
- [ ] **Phase 4** — std only at strengthen touch
- [ ] **Phase 5** — `width-audit.rish` in CI

---

*May the inventory shrink honestly, one module at a time, with the gate green at every step.*
