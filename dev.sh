#!/usr/bin/env bash
#
# dev.sh — THE single sanctioned way to preview bldgtyp.com locally.
#
# Serves a hot-reloading preview at http://127.0.0.1:1313/ and nothing else.
# Do NOT run `hugo server` by hand, a `python3 -m http.server`, or serve `site/`
# yourself. Those are the exact sources of the "why is it on a different port /
# why won't it hot-reload" confusion this script exists to eliminate.
#
#   ./dev.sh            run it, open http://127.0.0.1:1313/, Ctrl-C to stop
#
# Agents: run this in the background, then drive/inspect http://127.0.0.1:1313/.
# To regenerate the deployable static output in site/, run `hugo` (not this).
#
set -euo pipefail

PORT=1313
URL="http://127.0.0.1:${PORT}/"

cd "$(dirname "$0")"

# Guarantee we ALWAYS land on ${PORT}. Hugo silently falls back to 1314/1315…
# when the port is busy, which is how previews end up on mystery ports. Kill any
# prior hugo server and free the port first so the URL never moves.
pkill -f "hugo server" 2>/dev/null || true
if command -v lsof >/dev/null 2>&1; then
  pids="$(lsof -ti "tcp:${PORT}" 2>/dev/null || true)"
  [ -n "${pids}" ] && kill -9 ${pids} 2>/dev/null || true
fi

echo "──────────────────────────────────────────────"
echo "  bldgtyp.com — local preview"
echo "  ${URL}"
echo "  hot-reload on every save · Ctrl-C to stop"
echo "──────────────────────────────────────────────"

# --disableFastRender : full rebuild on every change so reload ALWAYS fires.
# --port/--bind/--baseURL : pinned, so the address never changes.
exec hugo server \
  --port "${PORT}" \
  --bind "127.0.0.1" \
  --baseURL "${URL}" \
  --disableFastRender
