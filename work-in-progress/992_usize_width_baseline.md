# 992 · Width Baseline — `usize` Elimination

**Stamp:** `20260621.070712`
**Policy:** `context/TAME_STYLE.md` · `gratitude/TIGER_STYLE.md` · `active-designing/970`
**Status:** ABSOLUTE BAN. Every `usize` in authored `.rye` is debt. The compiler fork eliminates it.

---

## The Law

**Rye has no `usize`. No exceptions.**

`usize` is an architecture-specific type that silently changes meaning between targets. Rye is forking from Zig. The Zig slice `[]T` with `len: usize` is inherited debt, not an acceptable pattern.

| Width | Use |
|-------|-----|
| **`u32`** | All lengths, indices, counts, offsets. Four billion elements — larger than any garden. |
| **`u64`** | Wire-persistent sizes, timestamps, MMIO addresses, cross-target quantities. |
| **`usize`** | **BANNED.** Not in struct fields, not in parameters, not in returns, not in locals, not at boundaries. |

Where Zig's `std` currently forces `usize` (slice `.len`, `buf[i]`), the seam casts (`const x: usize = @intCast(...)`) are **technical debt** to be eliminated by the compiler fork — not an acceptable pattern to keep.

---

## Current Debt

| File | `usize` hits | Status |
|------|-------------|--------|
| `rishi/src/main.rye` | 37 | Debt — largest file |
| `brushstroke/skate_grid.rye` | 18 (seam casts) | Phase 1b done (`235812`) |
| `caravan/chain.rye` | 2 (seam casts) | Phase 1b done (`235512`) |
| `comlink/hosted_wire.rye` | 12 | Debt |
| `aurora/src/deciding.rye` | 11 | Debt |
| `aurora/src/posted.rye` | 11 | Debt |
| `brushstroke/wayland_seed.rye` | 0 | Phase 1b done (`235812`) |
| `aurora/src/relay.rye` | 8 | Debt |
| `tally/gardens.rye` | 5 (seam casts) | Debt |
| `mantra/src/main.rye` | 5 | Debt |
| `tally/seed.rye` | 2 (seam casts) | Debt |
| `rye/src/main.rye` | 2 | Debt |
| `caravan/bounded.rye` | 2 (seam casts) | Debt |
| `caravan/twin.rye` | 2 (seam casts) | Debt |
| `caravan/seed.rye` | 0 | Clean |

**Gate:** `tools/width-check.rish` — scans all authored `.rye` for any `usize` token. Zero tolerance.

---

## The Fork Eliminates the Debt

The Rye compiler fork (F1–F5 in `970`) replaces Zig's slice type:

| Step | What | Status |
|------|------|--------|
| **F0** | Decide: literal ban | Done |
| **F1** | Compiler spike: Rye rejects `usize` keyword in `.rye` source | **Next** |
| **F2** | Authored corpus: zero `usize` in all published `.rye` | Blocked on F1 |
| **F3** | Rye-native std: `rye/lib` with `u32`/`u64` signatures | After F2 |
| **F4** | Bridge sunset: self-hosted `rye run` without Zig | After F3 |
| **F5** | Guest Zig: interop lane for third-party code | After F4 |

The 90 parity witnesses are the specification F3 satisfies. When F3 completes, `usize` does not exist in Rye.

---

## Known Issue: Enricher Wrong Functions

`tools/enrich_strengthening_docs.rye` grabs wrong functions by bare name (e.g., `Atomic.replace` instead of `mem.replace`). Fix: match by full module path. Re-run on all 86 docs.

---

*Every `usize` is debt. The fork pays it. No exceptions, no seam patterns, no boundary carve-outs.*
