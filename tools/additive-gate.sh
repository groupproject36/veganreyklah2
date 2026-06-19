#!/bin/sh
# additive-gate.sh — weigh whether a strengthening pass is purely invariant-stating.
#
# A pure strengthening adds only assertions, the `maybe` marker, and comments to
# existing code; it changes what the code SAYS, never what it DOES. This gate
# reads a commit's (or a range's) diff to Rye's std and reports whether every
# added and removed line is an assertion, a maybe, or a comment.
#
#   GREEN  — the pass is purely additive; safe by shape as well as by behavior.
#   REVIEW — the pass touches code beyond assertions and words; the gate shows
#            those lines so a person can confirm they are intended new code
#            (a deliberate new helper, say) rather than an accidental change.
#
# The parity gate (parity.sh) remains the deeper backstop: it proves behavior is
# identical regardless. This gate adds a second, structural assurance for the
# common case — a pass that only states what was already quietly true.
#
# Heuristic and line-based on purpose: small, fast, and transparent. See
# active-designing/998_strengthening_strategy.md (the gates).
#
#   usage:  tools/additive-gate.sh [<commit-or-range>]   (default: HEAD)
set -u

REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO" || exit 1

RANGE="${1:-HEAD}"
case "$RANGE" in
    *..*) ;;                       # already a range, e.g. A..B
    *) RANGE="${RANGE}~1..${RANGE}" ;;  # a single commit means its own change
esac

diff="$(git diff "$RANGE" -- rye/lib/ 2>/dev/null)"
if [ -z "$diff" ]; then
    echo "no std changes in ${RANGE} — nothing to weigh."
    exit 0
fi

# Walk the diff. Flag every added or removed line that is more than a blank line,
# a comment, an assertion, or a maybe. We anchor on the statement's start (after
# peeling a leading defer/comptime) so a function literally named assert or maybe
# is not mistaken for an assertion of one.
flagged="$(printf '%s\n' "$diff" | awk '
    /^\+\+\+/ || /^---/ { next }                       # skip file headers
    /^[+-]/ {
        sign = substr($0, 1, 1); body = substr($0, 2)
        t = body; sub(/^[ \t]+/, "", t); sub(/[ \t]+$/, "", t)
        if (t == "") next                              # blank line
        if (t ~ /^\/\//) next                          # // /// //! line comment
        if (t ~ /^\*/ || t ~ /^\/\*/ || t ~ /\*\/$/) next  # block-comment line
        sub(/^defer[ \t]+/, "", t)                     # peel a leading defer
        sub(/^comptime[ \t]+/, "", t)                  # peel a leading comptime
        if (t ~ /^(std\.debug\.)?assert\(/) next       # an assertion statement
        if (t ~ /^(std\.debug\.)?maybe\(/) next        # the maybe marker
        printf("  %s %s\n", sign, body)
    }
')"

if [ -z "$flagged" ]; then
    echo "GREEN: ${RANGE} is purely additive to std — assertions, maybe, and comments only."
    echo "       It changes what the code says, never what it does."
    exit 0
else
    echo "REVIEW: ${RANGE} touches std beyond assertions, maybe, and comments."
    echo "        Confirm each line below is intended new code (a deliberate helper,"
    echo "        say), rather than an accidental behavior change. The parity gate is"
    echo "        the backstop that proves behavior either way."
    echo
    printf '%s\n' "$flagged"
    exit 1
fi
