#!/usr/bin/env bash
#
# PreToolUse(Bash) guard for bt-homepage.
#
# Enforces the ONE sanctioned local-preview method (./dev.sh). Blocks ad-hoc
# static servers and direct `hugo server` invocations and points the caller
# back to ./dev.sh. Exit 2 tells Claude Code to block the tool call and show
# stderr to the agent.
#
# It does NOT block `hugo` (the build) — only ways of *serving/previewing* the
# site other than ./dev.sh. ./dev.sh runs `hugo server` as a subprocess, which
# the hook never sees, so the sanctioned path is unaffected.

cmd="$(cat | /usr/bin/python3 -c 'import sys, json; print(json.load(sys.stdin).get("tool_input", {}).get("command", ""))' 2>/dev/null || true)"

# Forbidden preview patterns (case-insensitive). `hugo server` and `open` are
# anchored to a command boundary (start, or after ; & | ( ) so that merely
# *referencing* the string — e.g. `pkill -f "hugo server"` for cleanup, or a
# `pgrep` diagnostic — is NOT blocked; only actually starting one is.
#   http.server / http-server / php -S / npx serve  → ad-hoc static servers
#   hugo server                                     → must go through ./dev.sh
#   open … site/….html                             → opening generated output directly
if printf '%s' "$cmd" | grep -Eiq 'http\.server|http-server|php[[:space:]]+-s|npx[[:space:]]+serve|(^|[;&|(])[[:space:]]*hugo[[:space:]]+server|(^|[;&|(])[[:space:]]*open[[:space:]].*site/.*\.html'; then
  {
    echo "BLOCKED — this repo has exactly ONE local-preview method."
    echo ""
    echo "    ./dev.sh    →  hot-reloading preview at http://127.0.0.1:1313/"
    echo ""
    echo "Not allowed: python http.server, a direct 'hugo server', serving site/,"
    echo "or opening site/*.html in a browser."
    echo "To regenerate deployable output only (no preview), run: hugo"
    echo "See CLAUDE.md > Dev Workflow."
  } >&2
  exit 2
fi

exit 0
