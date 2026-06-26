import { defineConfig } from "@playwright/test"

const port = Number(process.env.PLAYWRIGHT_PORT ?? "8001")
const baseURL = process.env.PLAYWRIGHT_BASE_URL ?? `http://127.0.0.1:${port}`
const useWebServer = process.env.PLAYWRIGHT_WEB_SERVER !== "false"

export default defineConfig({
  testDir: "./tests/e2e",
  use: {
    baseURL,
  },
  ...(useWebServer
    ? {
        webServer: {
          command:
            `UV_CACHE_DIR=/tmp/uv-cache CERTIFICATE_USE_MOCK_PROVIDER=true FRONTEND_DIST_DIR=../frontend/dist uv run python -m uvicorn certificate_app.main:app --host 127.0.0.1 --port ${port} --app-dir src`,
          port,
          cwd: "../backend",
          reuseExistingServer: true,
        },
      }
    : {}),
})
