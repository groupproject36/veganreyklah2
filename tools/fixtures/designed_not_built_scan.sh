#!/usr/bin/env sh
# designed_not_built_scan.sh — count functional specs in designed-not-built flight.
# Gated: wire into parity only after Kaeden rules Edit 5 for.
set -eu

count=0
for f in context/specs/*.md; do
  [ -f "$f" ] || continue
  if grep -qiE 'designed.*not yet built|designed-not-yet-built' "$f"; then
    echo "DESIGNED $f"
    count=$((count + 1))
  fi
done
if [ "$count" -gt 1 ]; then
  echo "FAIL count=$count"
else
  echo "OK   count=$count"
fi
