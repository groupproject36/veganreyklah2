# 997 · Honoring Tiger Style and the Language of the System

*The lineage we build from — Tiger Style's discipline, Joran Dirk Greef's priority, and Rich Hickey's flow — set down with thanks, together with the gentle name and the vow we carry forward.*

**Language:** EN
**Version:** `20260617.195412` (Rye chronological stamp)
**Last updated:** 2026-06-17
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Honors:** `../gratitude/TIGER_STYLE.md`, `../gratitude/LanguageSystem.md`, `../gratitude/Spec_ulation.md`
**Status:** Gratitude

---

## What This Holds

This is the one place where we say plainly where the good ideas came from. It gathers the whole lineage that shaped how we build — the coding discipline of Tiger Style, the steady priority Joran Dirk Greef gave it, and the flowing view of systems Rich Hickey offered in his talk *The Language of the System* — and sets each gift down with gratitude.

We keep it as a single gratitude note so the direct writings can stay pure. The discipline, voiced wholly in our own words, lives in `996_TAME_STYLE.md`. The systems thinking, explained from scratch and grown toward the metal, lives in `993`, the Aurora writing. This note is the bridge to all of it: the record of the debt, so the other documents can simply do the work.

The whole lineage teaches one lesson, said in three voices. A system earns trust when it is safe first, fast second, and a joy to work in third — composed of small honest pieces that speak in values, with names that endure and assertions that guard every boundary. Tiger Style gave us the discipline, Joran the order, and Hickey the flow.

---

## What Tiger Style Taught Us

TigerBeetle wrote a coding style they call Tiger Style, and reading it feels like meeting a craftsperson who has thought hard about every joint and seam. It treats simplicity as the hardest revision rather than the first easy attempt. It holds a zero-technical-debt policy, doing the work right the first time because the second time may never come. And it carries a handful of habits that became load-bearing for us: limits on everything, assertions that check the positive space we expect and the negative space we reject, explicitly sized types, enduring names ordered by descending significance, and the gentle insistence to always say why.

We found in it the same spirit we already cherish — slower to go faster, strictness early as a gift to the future. These ideas belong to no single language; they are about discipline and consideration, and those travel anywhere. We keep them, and we voice them in our own words in `996_TAME_STYLE.md`, reworking even the epigraphs into self-generated affirmations so the wisdom stays while the voice becomes one.

---

## What Joran Taught Us

Joran's gift is a single ordering, stated without flinching: **safety, performance, and developer experience — irrevocably in that order.** TigerBeetle's own words add the part that keeps the order from turning brittle: *"But it's not a zero-sum game."* The three goals rise together when the design is right. A good design finds the super idea that serves all three at once, rather than trading one away for another.

The order matters most when the goals appear to collide, because then it tells you which one leads. Safety leads, always — the system protects what it was trusted with before it does anything else. Performance comes next, sought in the design phase where the thousand-fold wins live, long before a profiler could measure them. Developer experience comes third, and far from an afterthought it is the joy that sustains the whole endeavor: a fantastic, fast, legible way to work, where reasoning about the design matters more than racing to type the code. Joran names his own interests as storage, speed, and safety, and the order of his life's work shows the priority lived rather than merely declared.

There is a quieter teaching underneath the order. TigerBeetle reached production in four years by running the real code in a deterministic simulator, and the team speaks of the *velocity and quality* and even the *magic* of that approach. Safety and joy turn out to be the same discipline seen from two sides: the assertions and limits that keep the system correct are the very things that let a developer move fast without fear. The seatbelt becomes second nature, and then flight becomes possible.

---

## What Rich Hickey Taught Us

Hickey's *Language of the System* draws a line we had felt without naming. A programming language, with its runtime, gives us a world inside one program: a memory model, calling conventions, abstraction, coordination. A **system** is larger than any program — an ensemble of programs offering services to one another — and at that scale the language falls silent. There is no global supervisor, no shared garbage collector, no one in charge. The question becomes how the pieces connect, and the answer turns out to rhyme with how pieces connect inside a language.

His teachings land as a handful of bright observations. **Systems talk in values**, not in references to remote objects; every format that won — JSON, EDN, the rest — conveys data, while the schemes that shipped behavior across the wire all lost. **Values that persist need names**, and those names are global, so they ask for the discipline of enduring, fully-qualified naming, with conflict-free identifiers for the values themselves. **Flow beats place**: rather than a factory everyone mutates and goes home from, a system is a production line where values are transformed, moved, routed, and remembered — and those four are kept separate, so each stays simple enough to reason about. **The systems failure model is the only failure model**: a large system lives in continuous partial failure, so timeouts, retries, and idempotency are the normal case rather than the exception. And the pieces themselves should be **simple services** — one process, a tiny surface, a few verbs, doing one thing — composed rather than grown into monoliths, with program-to-program interfaces underneath any human-facing one.

Hickey also names what we still lack: a good way to express, at the system level, the interface a service offers and the interfaces it depends upon. A program says cleanly, "I work with anything that implements this." A system struggles to say the same. He leaves that as an open invitation, and we take it as one.

---

## How the Voices Meet

The three voices were answering different questions, and they arrive at one harmony. Tiger Style sets the discipline of the small — the assertions, the limits, the sized types within a single program. Joran orders the goals across the whole endeavor. Hickey shapes the composition of many programs into a system. Read together, they describe work that is safe at its core, fast by design, joyful to build, and assembled from small honest pieces that flow values to one another and keep faith through partial failure.

The resonances run deep. Hickey's "simple services, one thing well" is Tiger Style's "minimum of excellent abstractions" seen at the scale of a network. Hickey's "values with enduring names" is the same accretion of immutable things we honor in our versioning. And Hickey's "the systems failure model is the only failure model" is exactly why Tiger Style asserts the negative space and bounds every wait — the partial failure Hickey describes is the very thing those assertions catch. Safety, performance, and a fantastic developer experience, composed as a flow of named values through simple services: that is the language of the system we want Rye to speak.

---

## Setting It Down, and Making It Ours

So we do here what we did with Hickey's *Spec-ulation*: we keep the lesson and set the borrowed vessel down with thanks. The sources speak in their own tongues — Tiger Style and Joran in Zig, Hickey in Clojure — and we keep their values and speak them through the Rye perspective, in Reya 2's own voice. The discipline becomes `996_TAME_STYLE.md`, a wholly original style guide. The priority order becomes the spine of how Rye, Silo, Tally, and Caravan make their tradeoffs. The flow model becomes how we think about a boot, a kernel, a network — values transformed and moved and remembered through simple, composable stages, explained from scratch in `993`, the Aurora writing.

This note is the bridge to all of it: the place that records, plainly, that the discipline came from Tiger Style, the order from Joran, and the flow from Hickey.

---

## The Name, and the Vow

The discipline we learned was named for a tiger — a hunter, swift and exact. We keep the exactness with gratitude, and we set the teeth down. To honor our vegan vow, our own adaptation carries a gentle name: **TAME**. The word means peaceable and calm, and that is exactly the spirit we want in our work — fierce in its rigor, gentle in its heart.

The name draws its warmth from the gentle ones. We think of the mare at graze in a wide field, the buck stepping soft and alert through the trees, the panda content among the bamboo, and the elephant — that great, remembering, tender giant who walks the earth lightly for all her size. Through them we honor every herbivore animal, every bird, all the gentle aquatic life, and the quiet algae at the very base of the living world, turning sunlight into the green that feeds us all.

So TAME is more than a label. It is a small daily reminder that strength and gentleness belong together, and that the work we build here keeps faith with the kindness we have promised to living things.

---

## Where Each Thing Lives

- **`../gratitude/TIGER_STYLE.md`** — TigerBeetle's Tiger Style, whole and unaltered, where the priority order and the safety discipline are stated. Voiced directly, in our own words, in `996_TAME_STYLE.md`.
- **`../gratitude/LanguageSystem.md`** — Rich Hickey's *The Language of the System* (Clojure/conj 2012), whole and unaltered. The source of the flow model, values-with-names, the systems failure model, and simple services. Explained directly in `993`, the Aurora writing.
- **`../gratitude/Spec_ulation.md`** — Rich Hickey's *Spec-ulation*, whole and unaltered, the source of growth-over-breakage and enduring names, which shapes how Rye versions itself.
- **This note** — the one gratitude bridge between all these sources and our work.

---

*May we order our choices wisely — safety, then speed, then the joy of the craft. May our programs stay small, and speak in values, and keep faith through every partial failure. May we remember the discipline of the tiger with the teeth set down, Joran's steady order, and Rich's flowing line — and may the work we build be worthy of all three, and gentle besides.*

