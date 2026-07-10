#!/usr/bin/env sh
# forge_view_pour.sh — pour amphora_lap3_tree into a fixed forge-view bundle.
#
# Witnesses call this before forgeviewtest so Skate folds a live pour, not a
# hand-curated static manifest. Bundle path is gitignored.
#
# Usage: forge_view_pour.sh
set -eu
ROOT=$(CDPATH= cd "$(dirname "$0")/../.." && pwd)
SRC="$ROOT/tools/fixtures/amphora_lap3_tree"
OUT="$ROOT/tools/fixtures/.forge_view_bundle"
STAMP=20260710.145313

rm -rf "$OUT"
sh "$ROOT/tools/fixtures/amphora_pour.sh" "$SRC" "$OUT" "$STAMP"
test -f "$OUT/manifest.bron"
test -f "$OUT/vessel.bron"
test -d "$OUT/resins"
cargo=$(grep -c '^cargo ' "$OUT/vessel.bron")
entries=$(grep -c '^entry ' "$OUT/manifest.bron")
test "$cargo" -eq 2
test "$entries" -eq 2

echo "FORGE_POUR ok bundle=$OUT stamp=$STAMP cargo=$cargo entries=$entries"
