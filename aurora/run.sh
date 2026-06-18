#!/bin/sh
# aurora/run.sh — build an Aurora stage with Rye, and wake it in an emulator.
#
# Usage: aurora/run.sh [stage]     (stage defaults to "seed")
#
# Builds aurora/src/<stage>.rye into a freestanding RISC-V binary with `rye build`
# and wakes it on qemu-system-riscv64 -machine virt. Each stage speaks over the
# console and powers the machine off cleanly (exit 0) — the simple, working base
# the rest of the boot grows from. Every stage shares one memory layout, layout.ld.
set -eu

stage="${1:-seed}"

here="$(cd "$(dirname "$0")" && pwd)"
repo="$(cd "$here/.." && pwd)"
cd "$repo"

src="aurora/src/${stage}.rye"
elf="aurora/.build/${stage}.elf"

if [ ! -f "$src" ]; then
    echo "aurora/run.sh: no such stage: $src" >&2
    exit 2
fi

# Rye needs its toolchain. Honor a pre-set RYE_ZIG; otherwise use the vendored
# Zig 0.16.0 kept beside the project, so a stage builds with no extra setup.
if [ -z "${RYE_ZIG:-}" ] && [ -x "vendor/zig-toolchain/zig" ]; then
    RYE_ZIG="$repo/vendor/zig-toolchain/zig"
    export RYE_ZIG
fi

mkdir -p aurora/.build

echo "building '${stage}' with rye build (freestanding riscv64) ..."
rye/bin/rye build "$src" \
    -target riscv64-freestanding-none \
    -mcmodel=medium \
    -fno-entry \
    -T aurora/layout.ld \
    -femit-bin="$elf"

echo "waking '${stage}' in qemu-system-riscv64 (machine virt) ..."
echo "----"
status=0
timeout 10 qemu-system-riscv64 -machine virt -bios none -nographic \
    -kernel "$elf" || status=$?
echo "----"
echo "qemu exited with status $status (0 means the hart asked the machine to rest)"
exit "$status"
