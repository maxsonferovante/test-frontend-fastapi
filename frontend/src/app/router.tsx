import { createBrowserRouter, RouterProvider } from "react-router-dom"

import { HomeRoute } from "@/routes/home"

const router = createBrowserRouter([
  {
    path: "/",
    element: <HomeRoute />,
  },
])

export function AppRouter() {
  return <RouterProvider router={router} />
}
