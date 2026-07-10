#!/usr/bin/env sh
# amphora_scrub_arrival.sh — cold scrub on arrival: verify vessel parent, Amber verify, restore.
#
# Usage: amphora_scrub_arrival.sh bundle_dir [source_tree_for_diff]
set -eu
ROOT=$(CDPATH= cd "$(dirname "$0")/../.." && pwd)
BUNDLE=${1:?usage: amphora_scrub_arrival.sh bundle_dir [source_tree]}
SRC=${2:-"$ROOT/tools/fixtures/amber_ring1_tree"}

VESSEL="$BUNDLE/vessel.bron"
MANIFEST="$BUNDLE/manifest.bron"
test -f "$VESSEL" || { echo "FAIL missing vessel"; exit 1; }
test -f "$MANIFEST" || { echo "FAIL missing manifest"; exit 1; }

parent=$(awk '/^parent / {print $2; exit}' "$VESSEL")
got=$(openssl dgst -sha3-256 -r "$MANIFEST" | awk '{print $1}')
test -n "$parent" || { echo "FAIL vessel missing parent"; exit 1; }
test "$parent" = "$got" || { echo "FAIL parent mismatch want=$got got=$parent"; exit 1; }
echo "PARENT ok $parent"

# Amphora vessel parse on metal (wreck rule already seated at lap 1).
vessel_bin="$ROOT/amphora/bin/vessel-core"
if ! test -x "$vessel_bin"; then
  mkdir -p "$ROOT/amphora/bin"
  env RYE_ZIG="${RYE_ZIG:-$ROOT/vendor/zig-toolchain/zig}" \
    "$ROOT/rye/bin/rye" build "$ROOT/amphora/vessel_core.rye" -femit-bin="$vessel_bin"
fi
"$vessel_bin" parse "$VESSEL" >/dev/null
"$vessel_bin" verify "$VESSEL" >/dev/null
echo "STAMP ok Kumara stamp_sig verified"

sh "$ROOT/tools/fixtures/amber_ring1_verify.sh" "$BUNDLE"

restore=$(mktemp -d)
trap 'rm -rf "$restore"' EXIT
sh "$ROOT/tools/fixtures/amber_ring1_restore.sh" "$BUNDLE" "$restore"
diff -r "$SRC" "$restore" >/dev/null

echo "SCRUB ok arrival cold-verify + restore bit-faithful"
