import { expect, test } from "@playwright/test";

test("searches certificates and filters mixed results", async ({ page }) => {
  await page.goto("/");
  await page
    .getByLabel(/buscar certificados por email/i)
    .fill("teste@gmail.com");
  await page.getByRole("button", { name: /buscar certificados/i }).click();
  await expect(page.getByText(/Maxson Almeida/i)).toBeVisible();
  await page.getByRole("button", { name: /sucesso/i }).click();
  await expect(page.getByText(/Maxson Almeida Ferovante/i)).toHaveCount(0);
});
