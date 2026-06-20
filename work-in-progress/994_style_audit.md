# 994 · Style Audit — TAME and Radiant since sweep `0963662`

**Stamp:** `20260620.155212` (audit run); filename is stable — no timestamp suffix.
**Scope:** Main-track arc (`143312`–`153812`): strengthening 9979–9987, Skate grid, parity-via-`rye run`, Rishi builtins, parser hyphen fix. Shipped at `155212`.
**Baseline:** Last Radiant sweep commit `0963662`; garden vocabulary sweep `c91253e`.

---

## TAME audit — `.rye` and `.rish`

**Files reviewed:** 22 (all uncommitted `.rye`/`.rish` in working tree).

| Check | Result |
|-------|--------|
| `init.garden` / no stray `init.arena` in our code | GREEN |
| Preconditions on paths (`path.len > 0`) in Rishi I/O | GREEN |
| Postconditions on strengthened std wrappers | GREEN (9979–9987) |
| Named errors in Rishi `EvalError` set | GREEN |
| Assertions state invariants (`// postcondition`, `// invariant`) | GREEN on new Skate, Rishi, corpus tests |
| `std.debug.assert` in corpus tests (parity pattern) | Consistent with existing corpus |

**Notes:** Corpus tests intentionally use `std.debug.assert` so strengthened postconditions run at parity time — same pattern as `alloc_print_test` and `mem_diff_test`. Inherited `ArenaAllocator` in std remains per `context/specs/inherited-names.md`.

**Verdict:** GREEN — no blocking TAME fixes required.

---

## Radiant audit — writings and code comments since `0963662`

**Docs reviewed:** strengthening passes 9979–9987, `995`, `996`, `998_ALMANAC`, Rishi README, session logs from this arc.

| Check | Result |
|-------|--------|
| Lead with what IS | GREEN on new strengthening logs |
| Avoid bare "but" where "yet/however" fits | GREEN (0 hits in new strengthening/wip md) |
| Active voice in pass records | GREEN |
| Code comments affirm capability | GREEN (`isWordHyphen`, parser reorder comments) |

**Verdict:** GREEN — no prose rewrites required for this arc.

---

## Gate proof at audit time

- `rishi run tools/parity.rish` — 24/24 GREEN
- Rishi regression suite (index-of, parser_hyphens, split, join, contains, arithmetic, ends-with) — GREEN

---

*May the root hold; may the prose stay warm; may each pass stay green on the way home.*
