#!/bin/sh
# parity-selftest.sh — prove the parity gate turns RED on a real divergence.
#
# The parity gate (parity.sh) asserts that Rye's std is behavior-identical to
# the baseline. A gate we have never seen fail is a gate we cannot yet trust.
# So here we build a deliberately TAMPERED std — SHA3's domain-separation byte
# changed (0x06 -> 0x07), which alters every SHA3 digest — and confirm that a
# corpus program's output differs against it. If the tamper slips through with
# identical output, this self-test fails loudly: the gate would be blind.
#
# Nothing real is touched. The tampered std is a temporary shadow tree of
# absolute symlinks back to rye/lib, with exactly one file replaced, removed on
# exit. See active-designing/998_strengthening_strategy.md (the gates).
set -u

REPO="$(cd "$(dirname "$0")/.." && pwd)"
ZIG="${RYE_ZIG:-$REPO/vendor/zig-toolchain/zig}"
BASELINE_LIB="$REPO/vendor/zig-toolchain/lib"
RYE_LIB="$REPO/rye/lib"
PROG="$REPO/rye/tests/sha3_512_test.rye"

[ -x "$ZIG" ] || { echo "no toolchain at $ZIG (set RYE_ZIG)"; exit 1; }

work="$(mktemp -d)"; trap 'rm -rf "$work"' EXIT
shadow="$work/lib"
mkdir -p "$shadow/std/crypto"

# Shadow the lib tree with absolute symlinks, descending only as far as the one
# file we tamper, so the build sees a real lib that differs in exactly one place.
for e in "$RYE_LIB"/*; do
    name="$(basename "$e")"; [ "$name" = std ] && continue
    ln -s "$(realpath "$e")" "$shadow/$name"
done
for e in "$RYE_LIB"/std/*; do
    name="$(basename "$e")"; [ "$name" = crypto ] && continue
    ln -s "$(realpath "$e")" "$shadow/std/$name"
done
for e in "$RYE_LIB"/std/crypto/*; do
    name="$(basename "$e")"; [ "$name" = sha3.zig ] && continue
    ln -s "$(realpath "$e")" "$shadow/std/crypto/$name"
done

# The single tamper: flip SHA3's domain-separation byte, changing every digest.
sed 's/0x06, 24/0x07, 24/g' "$RYE_LIB/std/crypto/sha3.zig" > "$shadow/std/crypto/sha3.zig"

# Guard against a no-op perturbation (e.g. if sha3.zig's shape changed upstream).
if cmp -s "$RYE_LIB/std/crypto/sha3.zig" "$shadow/std/crypto/sha3.zig"; then
    echo "INCONCLUSIVE: the perturbation changed nothing — sha3.zig may have shifted shape."
    exit 2
fi

zsrc="$work/prog.zig"; cp "$PROG" "$zsrc"
base_out="$("$ZIG" run "$zsrc" --zig-lib-dir "$BASELINE_LIB" 2>&1)"
tamp_out="$("$ZIG" run "$zsrc" --zig-lib-dir "$shadow" 2>&1)"

echo "baseline : $(printf '%s' "$base_out" | tail -1)"
echo "tampered : $(printf '%s' "$tamp_out" | tail -1)"
echo "---"
if [ "$base_out" != "$tamp_out" ]; then
    echo "GREEN: the gate turns RED on a real divergence — the tamper was caught."
    echo "       A passing parity run therefore means something."
    exit 0
else
    echo "FAILED: a tampered std produced identical output — the gate is blind. Fix before trusting it."
    exit 1
fi
