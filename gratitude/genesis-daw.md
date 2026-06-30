# Genesis — the digital audio workstation that birthed Zig

**License:** Inspiration only — not a dependency  
**Role for us:** Andrew Kelley's DAW hot loop is why **Zig exists**: a performance-critical path where Go's GC skipped audio, C++ memory bugs burned weeks, and Rust's rules cost a month on font rendering — so he built a language with explicit control, no hidden allocation, and joy in the craft.

**Clean room:** We honor the discipline — bound the loop, surprise it with no allocation, prove invariants at the seam — and we study bare-metal kin (clashos, HellOS) as kin to Aurora. We copy nothing from Genesis into our modules.

---

## What we carry forward

- **No C++ dependencies, no exceptions** in the performance path — only Zig and C where necessary.
- **The hot loop must never skip** — the same instinct as TAME: safety first, performance where the design lives, craft as joy.
- **Bare-metal Zig is possible** — Aurora and Rye OS on RISC-V share that horizon.

Kelley's public writing and talks on the DAW-to-Zig arc are the study surface; this note is gratitude, not a gitlink.
