import { defineConfig } from "@playwright/test"

export default defineConfig({
  testDir: "./tests/e2e",
  use: {
    baseURL: "http://127.0.0.1:8000",
  },
  webServer: {
    command:
      "UV_CACHE_DIR=.uv-cache CERTIFICATE_USE_MOCK_PROVIDER=true FRONTEND_DIST_DIR=../frontend/dist uv run python -m uvicorn certificate_app.main:app --host 127.0.0.1 --port 8000 --app-dir src",
    port: 8000,
    cwd: "../backend",
    reuseExistingServer: true,
  },
})
