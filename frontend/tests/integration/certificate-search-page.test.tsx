import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { vi } from "vitest";

import { Provider } from "@/app/providers";
import { HomeRoute } from "@/routes/home";

vi.mock("@/lib/api", () => ({
  fetchCertificates: vi.fn().mockResolvedValue({
    email: "teste@gmail.com",
    applied_filter: "all",
    total_count: 2,
    filtered_count: 2,
    has_success: true,
    has_failed: true,
    certificates: [
      {
        id: "060d543f-7c44-4370-97c6-ca54cae0bfc2",
        order_id: 3340,
        product_id: 3336,
        participant_name: "Maxson Almeida",
        participant_email: "teste@gmail.com",
        participant_document: "",
        certificate_url: "https://example.com/certificate.pdf",
        created_at: "2025-12-06T17:57:07.693972",
        updated_at: "2025-12-06T17:57:07.693972",
        success: true,
      },
      {
        id: "b21c7fc8-ed52-4ee8-8267-3b01fdbc7c59",
        order_id: 3272,
        product_id: 316,
        participant_name: "Maxson Almeida Ferovante",
        participant_email: "teste@gmail.com",
        participant_document: "",
        certificate_url: null,
        created_at: null,
        updated_at: null,
        success: false,
      },
    ],
  }),
}));

test("renders results after searching a valid email", async () => {
  const user = userEvent.setup();
  render(
    <Provider>
      <HomeRoute />
    </Provider>,
  );

  await user.type(
    screen.getByLabelText(/buscar certificados por email/i),
    "teste@gmail.com",
  );
  await user.click(
    screen.getByRole("button", { name: /buscar certificados/i }),
  );

  expect(await screen.findByText(/^Maxson Almeida$/i)).toBeInTheDocument();
  expect(
    screen.getByText(/Exibindo 2 de 2 certificados encontrados/i),
  ).toBeInTheDocument();
});
