# Gratitude Licenses — Clean-Room Discipline

`gratitude/` is a reading library, not a dependency. We study concepts; we never copy code.

## GPL projects (sixos, ai-jail, damus)

- Tracked as **gitlinks only** (commit pointers, mode 160000) — our git history never contains their source code
- Study design concepts only; never copy code or documentation into our modules
- **River** (GPL-3.0) is NOT cloned — study through public Wayland protocol specs and public project documentation only
- Our implementations are written from scratch in Rye, expressed through quarantined clean-room briefs in `active-designing/`

## Local-only clones (nix, s6, skalibs — NOT tracked by git)

- Cloned locally for reading; excluded from git tracking
- LGPL-2.1 (nix) and ISC (s6, skalibs) — permissive enough for study
- Never add these to git; they stay local

## Permissive projects (zig, dvui, urbit, tigerbeetle, sui, primal, manyana, infuse.nix)

- Safe to study freely — MIT, ISC, Apache 2.0, public domain
- Still write our own implementations; concepts enter through the clean room

## The clean-room path

External research (`external-research/`) studies the world with attribution. Active designing (`active-designing/`) names only our own modules. The boundary between reading and building is the boundary between `gratitude/` and `rye/`, and it is never crossed by code — only by understanding.
