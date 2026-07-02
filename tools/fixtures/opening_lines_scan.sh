#!/usr/bin/env sh
# opening_lines_scan.sh — hosted .rye canonical head (std / assert / print).
set -eu

scan() {
  f="$1"
  missing=""
  qualified_a=$(grep -c 'std\.debug\.assert(' "$f" 2>/dev/null || true)
  qualified_p=$(grep -c 'std\.debug\.print(' "$f" 2>/dev/null || true)
  has_assert=$(grep -c 'const assert = std\.debug\.assert;' "$f" 2>/dev/null || true)
  has_print=$(grep -c 'const print = std\.debug\.print;' "$f" 2>/dev/null || true)
  qualified_a=${qualified_a:-0}
  qualified_p=${qualified_p:-0}
  has_assert=${has_assert:-0}
  has_print=${has_print:-0}
  if [ "$has_assert" -eq 0 ]; then missing="${missing} assert-bind"; fi
  if [ "$has_print" -eq 0 ]; then missing="${missing} print-bind"; fi
  if [ "$qualified_a" -gt 0 ]; then missing="${missing} qual-assert=$qualified_a"; fi
  if [ "$qualified_p" -gt 0 ]; then missing="${missing} qual-print=$qualified_p"; fi
  if [ -n "$missing" ]; then
    echo "FAIL $f$missing"
  else
    echo "OK   $f"
  fi
}

for f in \
  tally/seed.rye tally/gardens.rye \
  caravan/seed.rye caravan/bounded.rye caravan/twin.rye caravan/chain.rye caravan/capabilities.rye \
  mantra/src/main.rye mantra/src/store.rye mantra/src/weave.rye mantra/src/diff.rye \
  rishi/src/main.rye brushstroke/seed.rye comlink/hosted_wire.rye
do
  scan "$f"
done
