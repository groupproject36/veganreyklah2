# The External-Research Stack

**Language:** EN
**Last updated:** 2026-06-28 (one-clock reorg, chunk 3)
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Status:** Foundation

---

## What This Folder Is

This is where curiosity lands. The `external-research/` folder holds our explorations — the questions we chase, the experiments we run, the outside systems we study, the findings we want to keep close. Each exploration earns its own file, written so a reader can follow it start to finish, the way every piece in this project is written.

This folder is allowed to be experimental, informal, and overgrown at times. It is open to the world: it may name other projects, draw inspiration freely, and cite its sources, with the original works kept whole in the `gratitude/` folder. That openness is its purpose, and it is exactly what sets it apart from its disciplined sibling, the `active-designing/` stack, which carries only our own names and one fixed external and accrues slowly and intentionally. Here we roam; there we decide.

This file is the foundation stone. It rests at the bottom of the stack and explains how the stack works, so that anyone who opens this folder for the first time understands the shape of it at a glance.

---

## Redirect stubs

When an exploration **lands** (mission complete) or **moves** to active-designing, the numbered file becomes a **stub** — a short redirect, not deleted, so old links keep working. Stubs say **Deprecated** or **Executed**, name the stamp, and point at the canonical home.

| Stub | Canonical home |
|------|----------------|
| `20260621-051612_rishi-shell-redirect.md` | `active-designing/20260619-051312_the-faithful-hand.md`, `rishi/README.md` |
| `20260621-051612_shell-scripting-tame-redirect.md` | `tools/parity.rish`, gate trio |
| `20260621-051612_recommended-architecture-redirect.md` | `active-designing/20260618-184912_recommended-architecture.md` |

**Width policy:** interim seam manual [`968`](20260621-050312_usize-boundary-not-design.md); fork north star [`967`](20260621-051312_literal-usize-ban-language-fork.md) + [`../active-designing/20260621-051312_explicit-width-in-rye.md`](../active-designing/20260621-051312_explicit-width-in-rye.md).

**Retired patterns** (do not reintroduce in new research): Bash `parity.sh`, Python doc enrichers, permanent Tier C `usize` as destination, `init.arena` in prose (use `init.garden`).

---

## One clock, one order

Dated explorations carry `YYYYMMDD-HHMMSS_short-slug.md`; living documents (`README.md`, `TAME_GUIDANCE.md`) carry no stamp. Full naming law: [`../context/specs/20260627-102012_one-clock-naming-law.md`](../context/specs/20260627-102012_one-clock-naming-law.md).

## Explorations (newest first)

| Stamp | Note | Meaning |
|-------|------|---------|
| *(living)* | [TAME Guidance](TAME_GUIDANCE.md) | Living — voiced TAME style canon (philosophy and full why) |
| `20260622-232912` | [964 · seL4 and Redox Through the TAME Rye Lens — Can We Improve Upon Them?](20260622-232912_sel4-redox-through-tame-rye.md) | Research |
| `20260621-070712` | [965 · The Rye Compiler Fork — How a Language Becomes Its Own](20260621-070712_rye-compiler-fork.md) | Research |
| `20260621-064612` | [966 · Brix vs Bron — When to Compose and When to Notate](20260621-064612_brix-vs-bron.md) | Research |
| `20260621-063112` | [968 · Prompt Caching, ZON, and What Bron Already Is](20260621-063112_prompt-caching-zon-brix.md) | Research |
| `20260621-051612` | [990 · Shells Through the TAME Lens — Redirect](20260621-051612_shell-scripting-tame-redirect.md) | Redirect stub — Deprecated (`051612`) — survey complete; conclusion implemented. |
| `20260621-051612` | [992 · The Recommended Path — Redirect](20260621-051612_recommended-architecture-redirect.md) | Redirect stub — Deprecated (`051612`) — superseded by the active-designing brief. |
| `20260621-051612` | [988 · Rishi — Redirect](20260621-051612_rishi-shell-redirect.md) | Redirect stub — Deprecated (`051612`) — mission landed. |
| `20260621-051312` | [967 · Literal `usize` Ban — Forking Rye as Its Own Width Model](20260621-051312_literal-usize-ban-language-fork.md) | Exploration — decision recorded; design siloed at `active-designing/20260621-051312_explicit-width-in-rye.md` |
| `20260621-050312` | [968 · `usize` Is a Boundary Type, Not a Design Type](20260621-050312_usize-boundary-not-design.md) | Exploration — seam policy for **Zig-ground era**; strategic fork recorded in [`20260621-051312_literal-usize-ban-language-fork.md`](20260621-051312_li |
| `20260620-040112` | [969 · Dual Editors and Priorities — What Two Agents Teach About Growing a System](20260620-040112_dual-editors-and-priorities.md) | Research |
| `20260620-020712` | [970 · Formats, Editors, Inference, and Tensors — What the Horizon Modules Inherit](20260620-020712_formats-editors-inference-and-tensors.md) | Research |
| `20260620-014412` | [997 · Honoring Tiger Style and the Language of the System](20260620-014412_system.md) | Gratitude |
| `20260620-010712` | [971 · Editors, Remoting, and the TAME Rye OS — Neovim, Kakoune, SSH, Mosh, and What We Build](20260620-010712_editors-remoting-tame.md) | Research |
| `20260620-010412` | [972 · Wayland, Compositors, and the TAME Desktop — What Brushstroke Inherits](20260620-010412_wayland-compositor-tame.md) | Research |
| `20260620-001412` | [973 · A Forge for Mantra — How Git, Weaves, and Group Projects Meet](20260620-001412_mantra-forge-and-group-projects.md) | Research |
| `20260619-225212` | [974 · s6, SixOS, Nix, and infuse — What Caravan, Brix, and Tally Inherit](20260619-225212_s6-sixos-nix-infuse.md) | Research |
| `20260619-220012` | [975 · Tablecloth — A TAME-Aligned Datastore: Close Reading of the Field](20260619-220012_tablecloth-tame-datastore.md) | What would a datastore look like if it were designed in the TAME order — correctness first, performance second, joy thir |
| `20260619-171112` | [976 · Microkernel or Monolith? — What Caravan Can Learn from seL4 and Redox, and What TAME Demands](20260619-171112_microkernel-vs-monolith-for-caravan.md) | Research |
| `20260619-155612` | [977 · POSIX at the Door — What the OS Interface Asks of TAME, and How River and Ghostty Show the Way](20260619-155612_posix-and-tame-guidance.md) | Research |
| `20260619-153612` | [978 · The Stack Toward a Living Desktop — Mantra, Tally, Tablecloth, Aurora, and Pond Grown for a Rishi Shell](20260619-153612_stack-toward-a-living-desktop.md) | Research synthesis and forward design |
| `20260619-153212` | [979 · Where Building Met Design — a Progress Map at the Turn](20260619-153212_where-building-met-design.md) | Survey |
| `20260619-070612` | [980 · Brushstroke and the Documentation Surface — a Drawn Interface for Rye, and How the System Shows Itself](20260619-070612_brushstroke-and-the-docs-surface.md) | Two strands, woven into one rope. The first is a plain question: should we begin documenting Rye OS in earnest — Rishi's |
| `20260619-035912` | [981 · One Identity, Many Keys — and a Fractal Address Space](20260619-035912_unified-keys-and-address-space.md) | A person today carries a fistful of keys — an SSH key to reach their machines, a GPG key to sign their work, a Sui key t |
| `20260618-212112` | [982 · A Content-Centric Messenger, From the Network In](20260618-212112_content-centric-messaging.md) | A message is a meaning meant for someone. This study designs the smallest honest way to carry one — content-named, encry |
| `20260618-204012` | [983 · Borrow Checking, the Garden, and Correctness by Construction](20260618-204012_borrow-checking-and-correctness.md) | A question worth asking carefully: would borrowing inspiration from Rust's borrow checker contradict TAME's love of stat |
| `20260618-195612` | [984 · A Devotional Social Layer, Kept Simple](20260618-195612_devotional-social-layer.md) | If `985` asks how a value crosses between two machines, this asks what we would build atop that for **people** — a small |
| `20260618-195512` | [985 · Encrypted Networking, From the Boot Upward](20260618-195512_encrypted-networking-riscv.md) | How does a machine come to speak to another machine — from the firmware that wakes it, through the boot, up into a runni |
| `20260618-190312` | [986 · Reading Aurora and Mantra Through the Decided Design](20260618-190312_decided-design-aurora-mantra.md) | Aurora (`993`) and Mantra (`998`) were written before the active-designing stack settled its principles — Gall's Law, th |
| `20260618-180812` | [987 · The Bounded Enclosure — How Rye, Tablecloth, Rishi, and Mantra Serve Pond, Caravan, and Tally](20260618-180812_pond-foundation.md) | Pond re-grows over the kernel's isolation primitives — and in our own world, those primitives are ours: **Caravan**, the |
| `20260618-150112` | [989 · One Language or More? Rye, the Shell, and the Voices of an OS](20260618-150112_voices-of-an-os.md) | Exploration |
| `20260617-201612` | [991 · Useful Utilities — What We Lean On, and What We'll Re-Grow](20260617-201612_useful-utilities.md) | Living roadmap |
| `20260617-195812` | [993 · Aurora: A Boot Designed for RISC-V](20260617-195812_aurora-boot-riscv.md) | Exploration |
| `20260617-195712` | [994 · Caravan, Tally, and the Shape of Networking](20260617-195712_caravan-tally-networking.md) | Exploration |
| `20260617-195612` | [995 · Ownerboot at the Reset Vector](yonder/20260617-195612_ownerboot-riscv-caravan.md) | Origin story — Caravan live; ownerboot sovereignty horizon; in `yonder/` |
| `20260617-195312` | [998 · Mantra: Version Control as a Weave](yonder/20260617-195312_mantra.md) | Origin story — module live; in `yonder/` |

## How To Add an Exploration

Adding research is a small, glad ritual:

- **Name the file with its stamp** in `YYYYMMDD-HHMMSS_short-slug.md` form, or as a living document when the work revises in place.
- **Name the slug for its subject.** A short, descriptive slug tells the reader where they are.
- **Write it in Radiant Style.** Lead with what you found. Favor active voice and affirmative framing. Weave the method together with its meaning, so the reader arrives at the insight through the description itself.
- **Say why.** Open with the question that prompted the exploration, so a future reader understands the motive as readily as the result.
- **Close when it is whole.** A finished exploration can end with a benediction or a plain summary of what we now know and what it opens next.

---



---

*May each question find its file. May the newest thought always greet the reader first. May this folder grow downward and upward at once — rooted in its foundation, reaching toward whatever we are curious about next.*
