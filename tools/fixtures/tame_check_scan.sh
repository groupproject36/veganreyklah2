#!/usr/bin/env sh
# tame_check_scan.sh — scan authored .rye for TH-2 textual rules.
set -eu

scan() {
  f="$1"
  a=$(grep -c 'std\.debug\.assert(' "$f" 2>/dev/null || true)
  t=$(grep -c "$(printf '\t')" "$f" 2>/dev/null || true)
  w=$(grep -c '[[:space:]]$' "$f" 2>/dev/null || true)
  s=$(grep -c 'Self = @This()' "$f" 2>/dev/null || true)
  a=${a:-0}
  t=${t:-0}
  w=${w:-0}
  s=${s:-0}
  if [ "$a" -gt 0 ] || [ "$s" -gt 0 ] || [ "$t" -gt 0 ] || [ "$w" -gt 0 ]; then
    echo "FAIL $f assert=$a self=$s tab=$t trail=$w"
  else
    echo "OK   $f"
  fi
}

for f in \
  tally/seed.rye tally/gardens.rye \
  caravan/seed.rye caravan/bounded.rye caravan/twin.rye caravan/chain.rye caravan/capabilities.rye \
  mantra/src/main.rye mantra/src/store.rye mantra/src/weave.rye mantra/src/diff.rye \
  rishi/src/main.rye brushstroke/seed.rye comlink/hosted_wire.rye \
  aurora/src/deciding.rye aurora/src/seed.rye
do
  scan "$f"
done
