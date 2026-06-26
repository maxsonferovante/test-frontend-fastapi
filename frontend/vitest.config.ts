import { defineConfig } from "vitest/config"
import react from "@vitejs/plugin-react"
import path from "node:path"

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  test: {
    environment: "jsdom",
    globals: true,
    include: ["tests/unit/**/*.test.ts", "tests/integration/**/*.test.tsx"],
    exclude: ["tests/e2e/**", "node_modules/**"],
    setupFiles: "./tests/setup.ts",
  },
})
