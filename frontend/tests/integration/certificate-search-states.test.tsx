import { render, screen } from "@testing-library/react"
import userEvent from "@testing-library/user-event"
import { vi } from "vitest"

import { Provider } from "@/app/providers"
import { HomeRoute } from "@/routes/home"

vi.mock("@/lib/api", () => ({
  fetchCertificates: vi.fn().mockRejectedValue(new Error("Tente novamente em instantes.")),
}))

test("shows validation and error states", async () => {
  const user = userEvent.setup()
  render(
    <Provider>
      <HomeRoute />
    </Provider>,
  )

  await user.click(screen.getByRole("button", { name: /buscar certificados/i }))
  expect(screen.getByText(/Informe um email para continuar/i)).toBeInTheDocument()

  await user.type(screen.getByLabelText(/buscar certificados por email/i), "invalid")
  await user.click(screen.getByRole("button", { name: /buscar certificados/i }))
  expect(screen.getByText(/Informe um email valido/i)).toBeInTheDocument()
})
