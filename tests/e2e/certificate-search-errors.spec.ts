import { expect, test } from "@playwright/test"

test("shows validation feedback for invalid email", async ({ page }) => {
  await page.goto("/")
  await page.getByRole("button", { name: /buscar certificados/i }).click()
  await expect(page.getByText(/Informe um email para continuar/i)).toBeVisible()
})
