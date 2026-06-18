#!/bin/bash
# parity.sh — the differential-parity gate of the strengthening-compiler.
#
# For each program in the corpus, run it against the pristine BASELINE standard
# library and against Rye's STRENGTHENED standard library, and confirm the
# outputs (and exit codes) match to the byte. A strengthening is safe only while
# this stays green: we add what the code SAYS, never what it DOES — so the
# observable behavior of every program must be identical on both libraries.
#
# This is the gate's smallest honest form, buildable now from what we already
# have. The corpus is small today and grows with every pass and every test.
#
# See active-designing/998_strengthening_strategy.md for why this comes first.
set -u

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ZIG="${RYE_ZIG:-$REPO/vendor/zig-toolchain/zig}"
BASELINE_LIB="$REPO/vendor/zig-toolchain/lib"   # pristine, as the toolchain shipped it
RYE_LIB="$REPO/rye/lib"                          # our std, strengthened in place
CORPUS_DIR="$REPO/rye/tests"

# The programs we already trust. Add to this list as the corpus grows.
corpus=(sha3_512_test.rye sha3_boundary_test.rye version_test.rye call_paths_test.rye)

[ -x "$ZIG" ] || { echo "no toolchain at $ZIG (set RYE_ZIG)"; exit 1; }

work="$(mktemp -d)"; trap 'rm -rf "$work"' EXIT
pass=0; fail=0
for name in "${corpus[@]}"; do
    src="$CORPUS_DIR/$name"
    if [ ! -f "$src" ]; then echo "MISSING   $name"; fail=$((fail + 1)); continue; fi
    # zig run wants a .zig extension; the .rye source is Zig for now, so copy it.
    zsrc="$work/${name%.rye}.zig"
    cp "$src" "$zsrc"
    base_out="$("$ZIG" run "$zsrc" --zig-lib-dir "$BASELINE_LIB" 2>&1)"; base_rc=$?
    rye_out="$("$ZIG" run "$zsrc" --zig-lib-dir "$RYE_LIB" 2>&1)"; rye_rc=$?
    if [ "$base_out" = "$rye_out" ] && [ "$base_rc" -eq "$rye_rc" ]; then
        echo "PARITY    $name"
        pass=$((pass + 1))
    else
        echo "DIVERGE   $name (baseline rc=$base_rc, rye rc=$rye_rc)"
        diff <(printf '%s\n' "$base_out") <(printf '%s\n' "$rye_out") | head -20
        fail=$((fail + 1))
    fi
done

echo "---"
echo "parity gate: $pass matched, $fail diverged across ${#corpus[@]} program(s)"
if [ "$fail" -eq 0 ]; then
    echo "GREEN: Rye's std is behavior-identical to the baseline across the corpus."
else
    echo "RED: a strengthening changed behavior — investigate before it lands."
fi
[ "$fail" -eq 0 ]
