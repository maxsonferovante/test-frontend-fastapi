import { StrictMode } from "react"
import { createRoot } from "react-dom/client"

import { AppRouter } from "@/app/router"
import { Provider } from "@/app/providers"
import "@/styles/globals.css"

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <Provider>
      <AppRouter />
    </Provider>
  </StrictMode>,
)
