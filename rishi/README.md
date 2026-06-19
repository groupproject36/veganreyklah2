# Rishi — the shell of the Rye ecosystem

**Version:** `20260619.044912` (chronological; later is larger)
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Status:** First version — small, runnable, and growing

---

Rishi is the interactive-and-scripting shell of the Rye ecosystem: terse for the
hand, typed for safety, a sibling of Rye that shares its value model. The name
is a seer who hears the human and speaks faithfully to the machine — which is a
shell's whole work. Scripts carry the `.rish` extension. The reasoning behind
the name and the design lives in `../external-research/988_rishi_shell.md` and
`../active-designing/996_growing_a_language.md`.

## What This First Version Does

This version is honest about its size. It reads a `.rish` script and runs it,
supporting:

- **Comments** — a line beginning with `#`.
- **`let` bindings** — `let name = "a string"`, `let name = 42`, `let flag = true`,
  or `let copy = other` to carry an earlier value forward.
- **`say`** — `say "text with ${name} woven in"`, interpolating each `${name}`,
  or `say name` to speak a bound value. Each `say` ends with a newline.
- **Lists** — `let xs = ["a" "b" "c"]`, written space-separated; a quoted element
  may hold spaces of its own. `say xs` shows `[a b c]`, and two lists are equal
  when their elements match in order.
- **Comparison** — `a == b` and `a != b` yield a boolean; unlike kinds simply
  differ. The operator is found outside any quoted string, so `==` inside `"text"`
  stays text.
- **`contains`** — `xs contains value` yields a boolean, so membership reads as a
  fact and can be a gate: `assert allowed contains here`.
- **`assert`** — `assert <expr>` makes a fact a gate: when the expression is a
  false boolean, the script stops, says why, and exits non-zero. An optional
  `else "message"` gives the reason to show.

A short example, `tests/hello.rish`:

```
let who = "Rye"
let year = 2026
say "hello from Rishi, sibling of ${who}!"
say "the year is ${year}"
```

## Build and Run

Rishi is written in Rye (`src/main.rye`) and built by Rye itself — `rye build` —
against Rye's own standard library, so the language we are growing, the language
we write it in, and the language that builds it are one and the same:

```sh
mkdir -p rishi/bin
export RYE_ZIG="$PWD/vendor/zig-toolchain/zig"   # the toolchain Rye builds with
rye/bin/rye build rishi/src/main.rye -femit-bin=rishi/bin/rishi

rishi/bin/rishi version
rishi/bin/rishi run rishi/tests/hello.rish
rishi/bin/rishi run rishi/tests/checks.rish   # booleans, comparison, and assert
rishi/bin/rishi run rishi/tests/lists.rish    # lists, contains, and equality
```

`tests/checks.rish` shows the comparison-and-assert pieces, and `tests/lists.rish`
the list-and-membership ones — each a run of facts that all hold. A false `assert`
instead stops the script, names the broken fact, and exits non-zero: the gate
behavior `parity.rish` will lean on.

## How It Grows

The first version is the seed; the destination is `parity.rish`, our parity gate
written in Rishi. Three of the pieces it asks for have now landed — the `==` that
compares, the `assert` that gates, and the **list** that holds a corpus (with
`contains` to test membership) — each arriving the Rye way, additive and proven,
one careful step at a time. Two remain: a `run` that returns a structured process
result, and `map` and `where` over a pipeline. Each shares Rye's value model, so a
value made in a Rye program and a value carried through a Rishi pipeline are the
same value.

Two north stars guide that growth. `tests/hello.rish` is what runs today;
`examples/pond.rish` is where we are headed — an illustrative sketch of Rishi
composing a sandbox policy as a value and opening a **Pond** enclosure over
Caravan's isolation and Tally's bounded gardens. The reasoning lives in
`../external-research/987_pond_foundation.md`.

A note on the horizon: this version speaks through the same channel our test
programs use, so its output sits beside theirs. Routing `say` to standard output
in its own right is a small, early refinement on the way.

---

*May Rishi hear us truly and speak without distortion — small today, and growing
gently into a shell worth living in.*
