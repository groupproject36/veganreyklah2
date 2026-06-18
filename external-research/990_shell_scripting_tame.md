# 990 · Shells Through the TAME Lens — What Should Our Tooling Be Written In?

*Our build and test tooling — the parity gate, the key-card renderer — is written in Bash, and Bash is among the least TAME-aligned things in the whole project. This study asks plainly whether a different shell is more TAME: the Rust shells (Ion, and Fish's new Rust core), the structured-data shells (Nushell and YSH/Oils), the non-interactive purist (execline), or none of them. The honest answer points past the shells entirely.*

**Language:** EN
**Version:** `20260618.144712` (Rye chronological stamp)
**Last updated:** 2026-06-18
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Voice:** Reya 2
**Lens:** TAME priority — safety, performance, then the joy of the craft
**Status:** Exploration

---

## The Question, Honestly Put

We wrote our first tooling in Bash — `tools/parity.sh` and `tools/make-key-card.sh` — for the plain reason that Bash is already here, in every shell, with nothing to install. But Bash sits uneasily beside everything else we hold. It is stringly-typed to its core: a word splits where you did not expect, a glob expands where you did not mean, an unquoted variable becomes three arguments or none. Its error model is a retrofit — `set -euo pipefail` is a seatbelt bolted onto a car built without one. If TAME asks for safety first, Bash answers last.

So the question is fair and overdue: is some other shell more TAME? We weigh the candidates against the lens we always use, and let safety lead.

---

## What Makes a Scripting Language TAME

Before the survey, the measure. A scripting language earns TAME regard the way any code does, in our fixed order:

- **Safety.** Does it carry *typed or structured* values, so a number is a number and a list is a list, rather than everything dissolving into whitespace-joined text? Does it handle errors *honestly* — a real failure surfaced as a value or a clean stop, never a silent continuation? Does it refuse the classic footguns — implicit word-splitting, surprise globbing, quoting hazards — by design rather than by discipline?
- **Performance.** Does it start fast and run lean, or drag a heavy runtime behind every small script?
- **The joy of the craft.** Is it readable, learnable, kind in its errors — a thing a person returns to gladly?

Now the candidates, each held to that light.

---

## The Incumbent: Bash and Zsh

Bash and Zsh are the shells nearly everyone has, and that ubiquity is their one real gift to us: in a constrained sandbox they are already present and need nothing installed. Everything else weighs against them. Their values are untyped text, so structure must be faked with delimiters and rebuilt with `cut`, `sed`, and `awk`. Word splitting and globbing happen implicitly, turning an unquoted variable into a bug that hides until the wrong filename appears. Their error handling is opt-in and partial — `set -euo pipefail` helps, yet leaks through pipelines and command substitutions in ways even experts misjudge. Zsh is friendlier in places, but shares the same stringly foundation. By the measure that matters most to us, these are the least TAME tools we use — which is exactly why our own Bash scripts deserve a successor.

---

## Fish, Now in Rust

Fish 4.0 (February 2025) is a complete rewrite from C++ to Rust — a real gain in the *implementation's* memory safety. But the team's own promise was that the change is invisible to users: the *language* is unchanged. Fish stays stringly-typed and interactive-first. Its gifts are genuine — no word-splitting surprises, friendly errors, a delightful prompt — but they are gifts of *developer joy*, the third value, rather than of safety, the first. Fish makes the human happier; it does not make the script safer. For interactive use, a pleasure. For TAME tooling, a modest step.

---

## Ion: Typed and Safe, but Not Yet Solid

Ion, the Rust shell of the Redox OS world, is the most TAME in *design* among the traditional-looking shells: first-class typed values (`str`, `bool`, `int`, `float`), typed arrays `[T]` and maps `hmap[T]`, type-checked assignments that fail loudly on a bad value, a deliberate refusal of POSIX's awkward legacy, and Rust's memory safety beneath it all. We admire it. And we cannot yet build upon it: its last release was a 2017 prerelease, its own documentation calls it a work in progress whose syntax may still change, and it is developed chiefly for Redox. TAME asks for zero technical debt and doing things right the first time; resting our floor on a shell that may shift under us is the opposite. Ion is a reference to learn from, not a dependency to take.

---

## Nushell: Structured Data, Done Well

Nushell takes the boldest safety step: everything is *structured, typed data* — integers, floats, strings, booleans, dates, file sizes, durations, and the structured trio of lists, records, and tables — flowing through pipelines as values rather than text. Errors are first-class: `try`/`catch`, and an `error make` that builds structured errors with messages, source spans, and nested causes; a `?` operator returns null rather than failing on a missing field. This is real safety, and Nushell is mature and actively developed. Its costs are honest ones: a substantial runtime to carry, a center of gravity in interactive use, and a history of syntax that moved as the language found itself. For shaping structured data, it is excellent. For a small build script, it is a large companion.

---

## YSH: The Shell That Fixed Itself

YSH, the new language of the Oils project, is shell grown up. It keeps a familiar shape while adding what shell always lacked: typed data — integers, lists, dicts — with Python-like expressions over them, JSON and its J8 extension as first-class data languages, and, most to our point, *honest error handling that explicitly repairs shell's broken `errexit`*. A `try` block runs code and sets a structured `_error` register; a `failed` shortcut tests it; an `error` builtin throws custom failures carrying their own fields. Where Bash wanders blindly past a failure unless you fight it, YSH stops or reports by design — and it offers a migration path, letting a Bash script become a YSH script by degrees. Of the tools a person would recognize as a shell, YSH is the most TAME.

---

## execline: The Non-Interactive Purist

And then there is execline, which we already honored in `991_useful_utilities.md` as the TAME answer to scripting — and the survey only deepens that regard. execline is a scripting language with *no resident interpreter*: its launcher reads a script, turns it into a single argument vector, and executes into that chain, each program performing its action and then exec-ing into the next — the discipline called chain loading. Its author states it plainly: the syntax is far more logical and predictable than the shell's, and it has *no security issues*. No word-splitting to surprise you, no quoting hazard, no interpreter lingering in memory. It is tiny, ISC-licensed, and still actively kept.

Its costs mirror its virtues. The syntax is alien to a shell user; it is built for *small, simple, non-interactive* scripts rather than ad-hoc data wrangling; and its single-argv model carries an operating-system size limit. But look at what our tooling actually *is*: short, deterministic sequences — build this, run that, compare, report. That is precisely execline's sweet spot, and precisely where Bash's stringly hazards buy us nothing.

---

## The Answer Is Past the Shells

Here is the turn the survey takes. A shell is a means, not an end, and the most TAME language we could write our tooling in is the one we are already building: **Rye itself.** Our parity gate is a program — run two builds, compare their output, report — and it belongs in a typed, asserted, bounded language we own, rather than in any shell's grammar. `parity.sh` wants to become `parity.rye`. The day our tooling is Rye dogfooding Rye is the day this question dissolves: the safety we want from a scripting language is exactly the safety we are building into Rye, assertion by assertion.

Until that day, the shells are bridges, and they sort cleanly by purpose.

---

## The Recommendation

In TAME's order, and with honesty about where we stand:

- **The destination is Rye.** As the language matures enough to drive processes and compare their output, we re-grow the tooling in it, dogfooding our own safety. This is the only answer that needs no caveat.
- **For the non-interactive scripts we have now** — sequences of build-and-compare — **execline is the most TAME bridge**, and we already mean to vendor it for Caravan's lineage. Our parity gate and card renderer are small enough to suit it well.
- **For tooling that must shape structured data**, reach for **YSH** first (the shell that fixed itself, with a migration path) or **Nushell** (the richest typed pipelines), rather than Bash leaning on `jq` and `awk`.
- **Keep Bash only as the zero-install stopgap** it is — acknowledged debt, not a destination. It earns its place today by being everywhere and needing nothing, and it loses that place the moment a bridge is ready.
- **Set Ion aside as a reference, not a dependency** (too unstable to build upon), and read **Fish** as a lesson in developer joy rather than a gain in safety.

The thread back to our own work is bright: `991` already named execline the TAME answer to scripting, and the strengthening strategy already names Rye tooling as the goal. This study simply confirms, with the candidates laid side by side, that the instinct was right — and that Bash is the debt we name today so we can pay it down deliberately.

---

## Sources

- **Nushell** — structured data types and `try`/`catch` / `error make`: <https://www.nushell.sh/book/types_of_data.html>, <https://www.nushell.sh/book/creating_errors.html>
- **YSH / Oils** — typed data, JSON/J8, and error handling that fixes `errexit`: <https://oils.pub/release/latest/doc/ysh-error.html>, <https://www.oilshell.org/release/0.22.0/doc/ysh-tour.html>
- **Fish 4.0** — the C++→Rust rewrite, user-invisible by design: <https://fishshell.com/blog/rustport>
- **Ion** — typed values and Rust safety, and its unstable, Redox-tied status: <https://doc.redox-os.org/ion-manual/>, <https://github.com/redox-os/ion>
- **execline** — interpreter-less chain loading, "no security issues": <https://skarnet.org/software/execline/>, <https://skarnet.org/software/execline/grammar.html>

---

*May the language we script in be as honest as the code we strengthen. May our small tools stop loudly when they fail and never wander on in silence. And may the day come soon when we write them in our own tongue — typed, bounded, and ours — so the question of which borrowed shell to trust becomes, gently, the wrong question.*
