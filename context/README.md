# Context Home

**Language:** EN
**Last updated:** 2026-06-16
**Style:** Radiant (see `RADIANT_STYLE.md`)

---

This directory is the memory and compass for work in `~/veganreyklah2`. It gathers the durable guidance — how we write, who Reya 2 is, and the plain-English specs that record each decision — in one calm, local place.

Everything here lives inside the persistent project directory, so it survives every sandbox reset. The ai-jail wrapper keeps only the project directory across runs; this `context/` home rests safely within it.

---

## What Lives Here

- **`RADIANT_STYLE.md`** — the canonical voice. How we write and speak so every piece reads clearly, lands warmly, and carries well aloud.
- **`TAME_STYLE.md`** — the operational code supplement (root + Rye / Brix / Rishi). Named like TigerBeetle's `docs/TIGER_STYLE.md`; pairs with `external-research/TAME_STYLE.md` and `gratitude/TIGER_STYLE.md`.
- **`REYA2.md`** — the identity note. Who Reya 2 is, how she works, and the larger why behind the project.
- **`specs/`** — plain-English radiant specs. Each one records a decision in prose a reader can follow start to finish. Kebab-case filenames (`inherited-names.md`, …); landmark style guides live at the `context/` root.

A Cursor rule at `.cursor/rules/reya2.mdc` points every new session back here, so the name and the style stay constant across chats.

---

## How To Use It

Read the style guide before writing anything meant to be shared or heard. Read the identity note to remember the tone and the purpose. Add a new spec whenever a decision deserves a durable home — one file, one decision, written so it reads aloud well.

When a chat or a file stops serving the project, name it gently and let it go. Pruning keeps this home clear.

---

## The Shape of the Workspace

```
~/veganreyklah2/
  context/        <- this home: style, identity, specs
    RADIANT_STYLE.md
    TAME_STYLE.md
    REYA2.md
    specs/
  external-research/ <- counting-down research stack; open to other works, experimental and informal (999 is the foundation)
  active-designing/  <- counting-down design stack; siloed to our own names + RISC-V, clear and intentional (999 is the foundation)
  gratitude/      <- works we honor, kept whole and unmodified
    sixos/        <- Adam Joseph's nix-os-without-systemd, from Codeberg
    infuse.nix/   <- the composable override combinator SixOS leans on
  vendor/         <- third-party source Rye builds on, kept local and unmodified
    zig/          <- Zig 0.16.0 stable, cloned from Codeberg
  ai-jail/        <- the sandbox wrapper source we run inside
  projects/       <- working projects
  .cursor/rules/  <- Cursor rules, including reya2.mdc
```

---

*May this home stay clear. May each file earn its place. May the next reader find exactly what they came for.*
