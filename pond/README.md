# Pond — The Enclosure and Its Applications

**Language:** EN
**Last updated:** 2026-07-02
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)

---

Pond holds **applications** that compose Rye OS modules above the kernel and compositor — the first ring where isolation policy meets a running whole a person can use. The `apps/` floor keeps enclosure code and application code apart.

**Enclosure horizon (Pond clause — Kaeden completes):** Pond's enclosure aspect **runs what Brix composes under policy**. This is the recommended completion; your true ending may refine the wording.

**First application:** [`apps/drawn_terminal.rye`](apps/drawn_terminal.rye) — SLC-2a Ring 3, the drawn terminal (Rishi session mirrored in a Brushstroke/Skate window).

Policy-as-value horizon: `rishi/examples/pond.rish` and `external-research/20260618-180812_pond-foundation.md`.

---

## Compile layout

Rye resolves modules from the compile directory. Under `pond/apps/`:

| Path | Points to |
|------|-----------|
| `rishi` | `../../rishi/src` |
| `brushstroke` | `../../brushstroke` |

These symlinks are required for `drawn_terminal.rye` to import `rishi/main.rye` and `brushstroke/wayland_seed.rye`.

---

## Build and run — drawn terminal

From the repository root:

```bash
mkdir -p pond/bin
export RYE_ZIG="$PWD/vendor/zig-toolchain/zig"
rye/bin/rye build pond/apps/drawn_terminal.rye brushstroke/xdg-shell-protocol.c \
  -Ibrushstroke -lc -lwayland-client -lrt \
  -femit-bin=pond/bin/drawn-terminal
```

| Mode | Command | Purpose |
|------|---------|---------|
| **Witness** | `pond/bin/drawn-terminal sessiontest` | Headless Ring 3 witness (golden lines, signatures, ceiling row) — in parity **140** |
| **Metalsmoke** | `pond/bin/drawn-terminal metalsmoke` | Automated Wayland slice — [`tools/slc2a_ring3_metal.rish`](../tools/slc2a_ring3_metal.rish) |
| **Live** | `pond/bin/drawn-terminal` | Interactive mirror on GNOME Wayland + stdin (keyboard-from-window: SLC-2b) |

**Metal close (Kaeden):** run live mode — type commands, idle ~one minute (pong), fill past the transcript ceiling (status row), exit with `:quit`.

---

*May each app rest above the modules it composes, and may the enclosure stay honest about what it grants.*
