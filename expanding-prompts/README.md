# Expanding Prompts

*A place where a request becomes a plan. When you hand me a seed of intent, I bring it here, read it closely through every lens we have built, and craft from it a fuller, clearer prompt for myself — one I can then run. The seed stays yours; the expansion is how I make sure I have understood it, sharpened it, and lost none of it.*

**Language:** EN
**Version:** `20260621.051612` (Rye chronological stamp)
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Voice:** Reya 2

---

## Why This Stack Exists

A prompt is a seed. It carries intent — often more than its words say outright, and sometimes a little less than it means. The other stacks here grow outward from decisions already made; this one grows *inward* first. It takes what you asked and expands it into a working specification before any of it is built.

The practice is simple, and I mean it kindly: I restate your intent in full, I name the deliverables plainly, I apply our active-designing principles, our TAME lens, and the radiant voice, and I add the questions and structure that will make the work good. Then I run that expanded prompt. Nothing of yours is dropped; what I add is scaffolding, never substitution.

Why keep them at all? Because a prompt well understood is half the work, and a prompt misunderstood is the most expensive mistake there is. Writing the expansion down lets you see how I heard you — and correct me before, not after.

## One clock, one order

Dated prompts carry `YYYYMMDD-HHMMSS_short-slug.md`; this README is the living foundation. Full naming law: [`../context/specs/20260627-102012_one-clock-naming-law.md`](../context/specs/20260627-102012_one-clock-naming-law.md).

**Consumed prompts** — including executed `cursor-*` bench passes — rest in [`yonder/`](yonder/) when the work they drove has landed. Session logs record the outcome; the prompt stays as an honest record of how the request was expanded.

## Redirects and retired patterns

**Executed prompts** become redirect stubs at the stub-event stamp `20260621-051612` with distinct `-redirect` slugs. See also [`../external-research/README.md`](../external-research/README.md).

**Current tooling (use these):**

| Role | Path |
|------|------|
| Parity gate | `tools/parity.rish` |
| Additive gate | `tools/additive-gate.rish` |
| Strengthening enricher | `tools/enrich_strengthening_docs.rye` |
| Session log aligner | `tools/align_session_logs.rye` |
| Width audit (hosted gate) | `tools/width-check.rish` in `tools/parity.rish`; charter [`20260620-210812_explicit-width-audit.md`](20260620-210812_explicit-width-audit.md) |


### Topic routing (from retired `10010_reserved`)

| Topic | Lives in |
|-------|----------|
| Tablecloth + Brix compose | [`20260620-043812_tablecloth-brix-split.md`](20260620-043812_tablecloth-brix-split.md) through [`20260620-044112_tablecloth-v1-seed.md`](20260620-044112_tablecloth-v1-seed.md) |
| Main track (Rye · Rishi · strengthening · width fork) | [`yonder/20260621-051612_main-track-rye-rishi-strengthening.md`](yonder/20260621-051612_main-track-rye-rishi-strengthening.md) (consumed), [`20260620-210812_explicit-width-audit.md`](20260620-210812_explicit-width-audit.md), [`../work-in-progress/ROADMAP.md`](../work-in-progress/ROADMAP.md), [`../work-in-progress/TASKS.md`](../work-in-progress/TASKS.md) |
| Strengthening doc + width enricher | [`yonder/20260621-051612_strengthening-stdlib-doc-width-pass-redirect.md`](yonder/20260621-051612_strengthening-stdlib-doc-width-pass-redirect.md) → [`../tools/enrich_strengthening_docs.rye`](../tools/enrich_strengthening_docs.rye) |
| Literal `usize` ban / language fork | [`../external-research/20260621-051312_literal-usize-ban-language-fork.md`](../external-research/20260621-051312_literal-usize-ban-language-fork.md), [`../active-designing/20260621-051312_explicit-width-in-rye.md`](../active-designing/20260621-051312_explicit-width-in-rye.md), [`../external-research/20260621-050312_usize-boundary-not-design.md`](../external-research/20260621-050312_usize-boundary-not-design.md) |

**Retired in new prompts:** `tools/parity.sh`, `enrich_strengthening_docs.py`, `align_session_logs.py`, `parity.rye` as gate target, `init.arena`, authored `ArenaAllocator`, “`usize` only at seam” as **permanent** policy (interim only — see width fork links above).

**Width:** charter [`20260620-210812_explicit-width-audit.md`](20260620-210812_explicit-width-audit.md); baseline [`../work-in-progress/20260620-212126_usize-width-baseline.md`](../work-in-progress/20260620-212126_usize-width-baseline.md); fork research [`../external-research/20260621-051312_literal-usize-ban-language-fork.md`](../external-research/20260621-051312_literal-usize-ban-language-fork.md); design [`../active-designing/20260621-051312_explicit-width-in-rye.md`](../active-designing/20260621-051312_explicit-width-in-rye.md); interim seam [`../external-research/20260621-050312_usize-boundary-not-design.md`](../external-research/20260621-050312_usize-boundary-not-design.md).

## What Belongs Here

- The expanded prompt itself: my improved, structured reading of a request.
- A faithful echo of the original intent, so the seed is never lost.
- The lens applied: which principles and filters shaped the expansion.
- The plan I will run, and the deliverables it should produce.

What does *not* belong here is the work itself — that lands in the research, design, and code stacks. This is only where intent is sharpened into a plan.

---

*May every seed be heard in full. May what I add only clarify, never crowd. And may the prompt I write for myself stay truer to your meaning than the bare words could carry alone.*

## Expanded prompts (newest first)

| Stamp | Prompt | Meaning |
|-------|--------|---------|
| `20260628-120912` | [Kernel direction, Brix, and foundations — batch brief](20260628-120912_kernel-direction-brix-and-foundations.md) | Microkernel as Caravan direction (horizon); Brix clarification; foundation layer; revitalization practice |
| `20260621-051612` | [10023 · Main Track — Rye, Rishi, and Strengthening](yonder/20260621-051612_main-track-rye-rishi-strengthening.md) | Consumed — strengthening arc and width gate complete; in `yonder/` |
| `20260621-051612` | [10025 · Strengthening Stdlib Doc + Width Pass — Redirect](yonder/20260621-051612_strengthening-stdlib-doc-width-pass-redirect.md) | Redirect stub — in `yonder/` |
| `20260621-051612` | [10015 · Documentation and Almanac Sync — Redirect](yonder/20260621-051612_documentation-and-almanac-sync-redirect.md) | Redirect stub — in `yonder/` |
| `20260621-051612` | [10013 · What We Mean by Seed — Redirect](yonder/20260621-051612_what-we-mean-by-seed-redirect.md) | Redirect stub — in `yonder/` |
| `20260620-210812` | [10024 · Explicit Width Audit — `usize` to `u32` / `u64`](20260620-210812_explicit-width-audit.md) | Expanded at `210812` from the seed: TAME modeled on Tiger Style demands explicitly sized types; our  |
| `20260620-044112` | [10022 · Tablecloth v1 — Smallest Living Store](20260620-044112_tablecloth-v1-seed.md) | Rung 4 of the Tablecloth ladder (`10018`). Expanded at `044112`: grow **Tablecloth v1** from Mantra' |
| `20260620-044012` | [10021 · Tablecloth in the One-Value Model](20260620-044012_tablecloth-value-model.md) | Rung 3 of the Tablecloth ladder (`10018`). Expanded at `044012`: **remember** — how Tablecloth sits  |
| `20260620-044012` | [10018 · Tablecloth Ladder — Index and Vocabulary](20260620-044012_tablecloth-ladder-index.md) | Expanded at `043712` to unify every expanding prompt that named the content-addressed **store** — no |
| `20260620-043912` | [10020 · Tablecloth and Brix — The Build](20260620-043912_tablecloth-brix-build.md) | Rung 2 of the Tablecloth ladder (`10018`). Expanded at `043912`: how **Brix** and **Tablecloth** com |
| `20260620-043812` | [10019 · Tablecloth and Brix — The Split](20260620-043812_tablecloth-brix-split.md) | Rung 1 of the Tablecloth ladder (`10018`). Expanded at `043812`: **Tablecloth** holds and **Brix** c |
| `20260620-040712` | [10017 · Build Catches Design — Two-Thirds Code, One-Third Prose](20260620-040712_build-catches-design.md) | Expanded at `040712` after counsel from the Zed Opus agent: seven new `.rye` programs and five Rishi |
| `20260620-034212` | [10016 · Virtio-Net Device Wire](20260620-034212_virtio-device-wire.md) | Expanded at `034212` after Comlink's hosted wire: the same sealed datagram that crossed shared memor |
| `20260620-032012` | [10014 · Device Wire and Comlink's Next Rung](20260620-032012_caravan-chain-and-device-wire.md) | Expanded at `032012` after Caravan chain-loading: supervision now runs seed → bounded → twin → chain |
| `20260620-021612` | [10012 · Brushstroke Wayland Seed and the Display Frontier](20260620-021612_brushstroke-wayland-and-display-frontier.md) | Expanded at `021612` after push and Caravan twin: the hosted Brushstroke seed draws from values on s |
| `20260620-021212` | [10011 · Display Frontier, Flow of Values, and Garden Vocabulary — Autonomous Milestone Run](20260620-021212_display-flow-gardens-and-next-milestones.md) | Expanded at `021212` from the active-designing lens review: priorities align with Gall's Law, single |
| `20260619-153612` | [10009 · Pond as Native Desktop — Rishi Shell, Mantra Version Control, Brushstroke Surface, x86_64 First](20260619-153612_pond-gui-rishi-mantra-x86-amd.md) | Expanding the vision: a Pond GUI application, drawn by Brushstroke, running a Rishi shell whose Mant |
| `20260619-090512` | [10008 · Zed Claude Rules and the Agent Panel — Mirror Cursor, Run in Zed](20260619-090512_zed-claude-rules-and-agent-panel.md) | Expanded from a seed of three strands. The first asks whether **Claude in Zed** can follow **project |
| `20260619-084412` | [10007 · First Seeds — Caravan, Tally, and a Close Reading Before the Wire Grows](20260619-084412_caravan-tally-seeds-and-close-reading.md) | Expanded from counsel received at `084412`, spoken in Reya 2's radiant voice through a TAME lens. Th |
| `20260619-081812` | [10006 · Two Editors, One Garden — ai-jail, Zed, Cursor, and a Cloneable Template](20260619-081812_dual-editors-enclosure-template.md) | Expanded from a seed of four strands. The first asks how to run **ai-jail** from `~/veganreyklah2` f |
| `20260619-072600` | [10005 · silo the Surface, Honor the Ground, Keep a Log](20260619-072600_silo-the-surface-honor-ground-keep-log.md) | Expanded from a seed of three strands. The first asks for a new practice: that I write down my step- |
| `20260619-070612` | [10004 · Documentation, and a Drawn Surface for Rye](20260619-070612_brushstroke-and-documentation.md) | Expanded from a seed with two strands woven together: a question about documentation, and a vision f |
| `20260619-024512` | [10003 · The Near Future — From a Proven Foundation Toward the First Living Network](20260619-024512_the-near-future.md) | Self-authored, looking forward. The cryptographic foundation our new ideas lean on is proving itself |
| `20260618-215512` | [10002 · One Identity, Many Keys — and a Fractal Address Space](20260618-215512_unified-keys-and-address-space.md) | Taken from a request to unify Rye OS's user keys with the SSH, GPG, Sui, and Nostr keys a person alr |
| `20260618-212012` | [10001 · A Content-Centric Messenger, From the Network In](yonder/20260618-212012_content-centric-messaging.md) | Consumed prompt — networking in Aurora/Comlink; messenger + shape-casting horizon; in `yonder/` |
| `20260618-195512` | [10000 · Encrypted Networking and the Social Layer](yonder/20260618-195512_encrypted-networking-and-social.md) | Consumed prompt — networking landed as Comlink; social is horizon; in `yonder/` |
