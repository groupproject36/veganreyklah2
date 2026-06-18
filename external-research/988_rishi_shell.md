# 988 · Rishi — A Shell for the Rye Ecosystem, and the Parity Gate Three Ways

*We write `tools/parity.sh` in Bash today. This piece asks what it becomes as it grows toward TAME: first in execline (the no-surprise bridge), then in Rye itself (typed and owned, but heavy for glue), and then in a shell made for our own ecosystem — **Rishi**, with `.rish` scripts — which unites execline's safe execution with Rye's typed values in a surface terse enough for a human's hand. The parity gate turns out to be the perfect first proving-ground, because it is part orchestration and part data, and shows exactly where each tool shines and strains.*

**Language:** EN
**Version:** `20260618.160612` (Rye chronological stamp)
**Last updated:** 2026-06-18
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Voice:** Reya 2
**Lens:** TAME priority — safety, performance, then the joy of the craft
**Status:** Exploration
**Builds on:** `989_voices_of_an_os.md`, `990_shell_scripting_tame.md`, `991_useful_utilities.md`

---

## Mission

To name and sketch the shell of the Rye ecosystem — the language a person reaches for to compose flows, run tools, and orchestrate small work — so that the scripting around our project grows as safe, as clear, and as *ours* as the code it tends. The near mission is concrete: carry `tools/parity.sh` off Bash and toward something TAME. The far mission is a shell, **Rishi**, that a person can love and trust in equal measure.

---

## Problem

Two problems meet in one small script.

First, Bash is the least TAME thing we use (`990` lays out why): untyped text, implicit word-splitting, a bolted-on error model. Our parity gate deserves better than the language most likely to betray it quietly.

Second — and this is the subtler one — **the parity gate is two kinds of work wearing one coat.** Part of it is *orchestration*: for each program in the corpus, run it against the baseline library, then against ours. That part wants execline's spirit — a predictable sequence of process hand-offs with no surprises. The other part is *data*: compare two outputs, keep a running tally of matched and diverged, and report a single verdict at the end. That part wants typed values and honest aggregation. No borrowed shell does both halves well, and the systems language that could (Rye) is too ceremonious for a glue task. The script sits exactly on the seam `989` drew between orchestration and typed-data work.

---

## Opportunity

That seam is the opportunity. If we had a shell that joined **execline's safe, no-surprise execution** to **Rye's typed value model**, in a surface as terse as Bash, the parity gate would have a natural home — orchestration that never surprises, comparison and tally that never lie, and a script a person can read in one breath. That shell is what we name here: **Rishi**, writing `.rish`. And the parity gate is the ideal first thing to write in it, because it stresses both halves at once.

---

## On the Name: Rishi and `.rish`

A *rishi* is a seer — one who *hears* the truth (śruti) and *speaks* it faithfully. That is a shell's whole vocation: it hears the human and speaks to the system, carrying intent across the boundary without distortion. The name also carries the gentleness this project is vowed to — the bhakti tradition's devotion and its sattvic, plant-kind way of living — so the tool that sits closest to a person's hand is named for care rather than command.

The extension `.rish` was chosen with eyes open. `.rsh` was set aside deliberately: across the developer community those three letters read instantly as `rsh`, the classic Unix **remote shell**, and an extension that lies about a file's nature is exactly the kind of quiet confusion TAME refuses. `.rish` carries no such canonical baggage; its only echo is a niche Android helper (Shizuku's "Rish"), in a different domain and a different community, weak enough to set aside. And `.rish` reads as *family* — it stands beside `.fish`, `.ksh`, `.zsh`, and `.csh` and announces plainly, *this is a shell language*. Since we are building our own OS, we hold our own namespace; should we ever want the idea of a "remote shell," we will give it a name of our own rather than borrow back the one we declined. The direction stands, gladly and without veto.

(In `989` we floated *Brook* as a placeholder for this shell, "to argue over, not a decree." Rishi is the argument settled. Brook can rest, or live on as the name for the *stream of typed values* a Rishi pipeline carries — a small poetry, not a second tool.)

---

## Architecture: The Parity Gate, Three Ways

The same gate, rendered in three languages, shows the design plainly.

### In execline — safe execution, awkward aggregation

execline expresses the *orchestration* beautifully. A sketch (illustrative; execline leans on tiny companion utilities for tests and comparisons):

```
#!/usr/bin/execlineb -S0
forx -E prog { sha3_512_test sha3_boundary_test version_test }
backtick -E base { zig run rye/tests/${prog}.zig --zig-lib-dir baseline }
backtick -E ours { zig run rye/tests/${prog}.zig --zig-lib-dir rye/lib }
ifelse { s6-test "${base}" = "${ours}" }
  { echo "PARITY  ${prog}" }
  echo "DIVERGE ${prog}"
```

Read it and the virtues are clear: no word-splitting, no resident interpreter, every substitution explicit, the sequence exactly what it says. This is the no-surprise execution we want.

But read it again for what is *missing*. There is no running tally — no clean way to count *matched* and *diverged* across the loop, because each pass of `forx` execs forward into a fresh chain and keeps no mutable accumulator. There is no single final verdict, no overall exit code that reflects "any divergence at all," without resorting to a counter file on disk. And comparing two multi-line outputs through environment variables strains against env size limits. execline shines at *do this, then this, then this*; it strains at *gather, count, and judge*. That strain is the lesson, not a flaw.

### In Rye — typed and owned, but heavy

Rye can do the whole job, tally and all, as a real checkable program (Rye is Zig-shaped today, so this reads as Zig):

```zig
const corpus = [_][]const u8{ "sha3_512_test", "sha3_boundary_test", "version_test" };
var matched: u32 = 0;
var diverged: u32 = 0;
for (corpus) |prog| {
    const base = try run(io, .{ zig, "run", testPath(prog), "--zig-lib-dir", baseline_lib });
    const ours = try run(io, .{ zig, "run", testPath(prog), "--zig-lib-dir", rye_lib });
    if (std.mem.eql(u8, base.out, ours.out) and base.code == ours.code) matched += 1 else diverged += 1;
}
assert(matched + diverged == corpus.len); // every program accounted for
```

Here the tally is honest, the loop is bounded, the invariant is asserted, the comparison is exact. This is the safety we want. But it is *heavy*: spawning, capturing, allocation, and error handling are all spelled out, because a systems language is built to spell them out. For a program that runs for a microsecond on a server, that weight is right. For a glue script, it is a wall to climb each time.

### In Rishi — the sweet spot

Rishi keeps Rye's honesty and execline's safety, in a surface as quick as the Bash we started with (illustrative syntax, to argue over):

```
# parity.rish — the gate, in the Rye ecosystem shell
let corpus = ["sha3_512_test" "sha3_boundary_test" "version_test"]

let results = corpus | map prog => {
    name:   prog,
    parity: (zig run (test prog) --zig-lib-dir $baseline)
            == (zig run (test prog) --zig-lib-dir $rye_lib),
}

let diverged = results | where (not .parity)
say "parity: ${results.len - diverged.len} matched, ${diverged.len} diverged"
assert diverged.empty?  else  red "a strengthening changed behavior"
```

Three things make this Rishi rather than Bash. The values are *typed and structured* — `results` is a list of records, not whitespace-joined text. The `(zig run …)` call returns a *structured result* whose `==` compares output and exit code together, so there is no stringly hack merging stderr by hand. And the gate is an *assertion*, the same `assert` Rye and TAME lean on everywhere, turning the script's promise into a checked one.

### How the three overlap

The point is not three rival tools but one layered design:

- **execline gives Rishi its execution model.** Where a Rishi script spawns and sequences processes, it can *lower* to execline-style chain-loading underneath — inheriting the no-surprise, no-resident-interpreter safety for free. Rishi's orchestration *is* execline's spirit, wearing a friendlier face.
- **Rye gives Rishi its values.** A record, a list, a string, an `assert` in Rishi are *the same things* as in Rye — one value model, shared. A value made by a Rye program flows into a Rishi pipeline without being flattened to text and reparsed; the seam `989` warns of never opens. Rishi is, in a real sense, Rye's value model wearing a shell's clothes.
- **So the parity gate finds its home.** Its orchestration half rests on execline's safety; its data half rests on Rye's types; its surface is shell-terse. The two kinds of work that strained every single tool compose cleanly when the tool is built for both.

---

## Caveats

We name the hazards honestly, so the dream does not run ahead of the work.

- **Rishi does not exist yet.** Today the parity gate is Bash; the *near* bridge for orchestration-shaped scripts is execline (which we already mean to vendor); Rishi is the destination, not the present. We must not write `parity.rish` as if it ran.
- **Designing a language is a large vow.** A shell is small to use and large to build well. The danger is bikeshedding Rishi's syntax while the strengthening work waits. Rishi earns its hours only after the gates and the foundation are sound.
- **The syntax above is a sketch to argue over,** not a specification. Its only firm commitments are the three principles — typed values, structured process results, assertions as gates — not the particular punctuation.
- **`.rish` carries a faint echo** (the Shizuku "Rish"); we judge it weak, but we record it so the choice is informed rather than blind.
- **Interactive and scripted use still differ.** A REPL wants even more forgiveness than a script; Rishi must serve both without becoming two languages, and that tension is real work left to do.

---

## Longer Horizon

Further out, Rishi is the daily shell of Caravan: a person at the prompt composing typed flows, scripts that lower their orchestration to execline-clean chains for init and supervision, values that pass to Rye programs and back without a seam, and a history kept by Mantra in the same content-addressed weave that holds everything else (`989`). The whole family — Rye for programs, Silo for configuration, the execline-spirit layer for bringing the system up, Rishi for the human's hand, Mantra for memory — speaks several languages in one voice, because they share one value model all the way down. And perhaps, in time, an interactive Rishi that completes, suggests, and explains as kindly as the friendliest shells, while never once lying about a type or swallowing an error.

---

## Conclusion

The path is clear and unhurried. **Bash** holds the floor today, named honestly as debt. **execline** is the near bridge for the orchestration-shaped scripts, safe and surprise-free. **Rye** stands ready for any glue that needs full typed depth. And **Rishi** — `.rish`, the seer's shell — is the destination for the typed, terse, composition-first layer a person lives in, uniting execline's safe execution with Rye's honest values. The parity gate is the lighthouse we steer by: small enough to write soon, rich enough to prove the whole design, and dear enough to be worth doing with love.

---

*May the shell we build hear us truly and speak to the machine without distortion. May it carry our values whole, from the prompt to the program and back. And may Rishi, when it comes, be gentle in the hand and honest to the bone — a seer's tongue for a kind machine.*
