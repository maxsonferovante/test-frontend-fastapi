#!/usr/bin/env bash
set -euo pipefail

PORT="${PLAYWRIGHT_PORT:-8011}"
BASE_URL="http://127.0.0.1:${PORT}"

export UV_CACHE_DIR="${UV_CACHE_DIR:-/tmp/uv-cache}"
export PLAYWRIGHT_WEB_SERVER=false
export PLAYWRIGHT_BASE_URL="${PLAYWRIGHT_BASE_URL:-$BASE_URL}"

npm run build

UV_CACHE_DIR="${UV_CACHE_DIR}" \
CERTIFICATE_USE_MOCK_PROVIDER=true \
FRONTEND_DIST_DIR=../frontend/dist \
uv run --directory ../backend python -m uvicorn certificate_app.main:app --host 127.0.0.1 --port "${PORT}" --app-dir src &
server_pid=$!

cleanup() {
  kill "${server_pid}" >/dev/null 2>&1 || true
}
trap cleanup EXIT

for _ in $(seq 1 50); do
  if curl --fail --silent --show-error "${PLAYWRIGHT_BASE_URL}" >/dev/null; then
    break
  fi
  sleep 0.2
done

playwright test
