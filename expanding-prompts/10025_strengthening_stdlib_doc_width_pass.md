# 10025 · Strengthening Stdlib Doc + Width Pass

*Expanded at `031812`: pause new `k` strengthening; walk every `strengthening-compiler/` pass, match it to the Rye `std` surface it strengthened, embed signatures as code blocks, and record explicit-width policy per function in `992`.*

**Language:** EN
**Version:** `20260621.031812` (Rye chronological stamp)
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Voice:** Reya 2
**Lens:** TAME · `992` · `10024` · `9999`

---

## The Seed

> Take a break from new strengthening. Pass through all existing strengthening-compiler writings, match the functions they cover, add Rye std signatures in code blocks (our growing stdlib documentation folder), and do explicit-width fixing / inventory for those surfaces. Fold into `992_usize_width_baseline` or a sibling crosswalk. Expand into a prompt and run it.

## What This Pass Is

Not a parity witness pass — a **documentation and width audit** pass:

1. **Every strengthening doc** gains `## Rye std surface` (signatures from `rye/lib/std`) and `## Width notes` (Phase 4 policy per surface).
2. **`992_strengthening_width_crosswalk.md`** — machine-readable index linking pass number → doc → function → width tier.
3. **`992_usize_width_baseline.md`** — extended with Phase 4 strengthening subsection and link to crosswalk.
4. **Named internal bounds** in already-strengthened `mem` functions — `max_*_check` constants become `u32` with `assert` at the slice seam (no public signature changes).
5. **`tools/enrich_strengthening_docs.py`** — rerunnable enricher for future passes.

## Discipline

- **No new witnesses** this run — parity must stay **86/86** green.
- **Do not rename inherited Zig public signatures** — `usize` stays on `[]T` APIs; narrow inside the body only.
- **Strengthening pauses** at **9916** until the next `k <stamp>`; width braid on `caravan/chain` continues in parallel.

## Deliverables

- [x] This prompt (`10025`)
- [ ] Enrich all `strengthening-compiler/*.md` (except `9999` manifesto)
- [ ] `992_strengthening_width_crosswalk.md`
- [ ] Update `992_usize_width_baseline.md`
- [ ] `u32` named bounds in strengthened `mem` snapshot paths
- [ ] `995` / `996` — note documentation pass + strengthening pause
- [ ] Session log; commit + push all remotes

## Cross-Links

| Topic | Lives in |
|-------|----------|
| Width charter | `10024` |
| Baseline inventory | `992_usize_width_baseline.md` |
| Strengthening method | `9999_STRENGTHENING.md` |
| Enricher script | `tools/enrich_strengthening_docs.py` |

---

*May every pass name its surface, and every count name its width before the next strengthening earns a witness.*
