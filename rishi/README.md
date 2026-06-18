# Rishi — the shell of the Rye ecosystem

**Version:** `20260618.175012` (chronological; later is larger)
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
- **`let` bindings** — `let name = "a string"` or `let name = 42`.
- **`say`** — `say "text with ${name} woven in"`, interpolating each `${name}`,
  or `say name` to speak a bound value. Each `say` ends with a newline.

A short example, `tests/hello.rish`:

```
let who = "Rye"
let year = 2026
say "hello from Rishi, sibling of ${who}!"
say "the year is ${year}"
```

## Build and Run

Rishi is implemented in Rye and built against Rye's own standard library, so the
language we are growing and the language we build it in are one and the same:

```sh
mkdir -p rishi/bin
vendor/zig-toolchain/zig build-exe rishi/src/main.zig \
  -femit-bin=rishi/bin/rishi --zig-lib-dir rye/lib

rishi/bin/rishi version
rishi/bin/rishi run rishi/tests/hello.rish
```

## How It Grows

The first version is the seed; the destination is `parity.rish`, our parity gate
written in Rishi. Reaching it asks for a handful more: list values, a `run` that
returns a structured process result, `map` and `where` over a pipeline, the `==`
that compares, and `assert` used as a gate. Each arrives the Rye way — additive,
proven, one careful step at a time — and each shares Rye's value model, so a
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
