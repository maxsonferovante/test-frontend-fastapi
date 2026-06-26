import { expect, test } from "@playwright/test"

test("loads the packaged application shell", async ({ page }) => {
  await page.goto("/")

  await expect(
    page.getByText(/certificate search control room/i),
  ).toBeVisible()
  await expect(
    page.getByRole("heading", { name: /consulte certificados por email/i }),
  ).toBeVisible()
})

test("falls back to the spa route after a direct navigation", async ({
  page,
}) => {
  await page.goto("/search/certificate")

  await expect(
    page.getByText(/certificate search control room/i),
  ).toBeVisible()
  await expect(
    page.getByRole("heading", { name: /consulte certificados por email/i }),
  ).toBeVisible()
})
