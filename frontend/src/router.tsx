import CalendarPage from "pages/CalendarPage";
import HomePage from "pages/HomePage";
import SearchPage from "pages/SearchPage";
import { createBrowserRouter } from "react-router-dom";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <HomePage />,
  },
  {
    path: "/search",
    element: <SearchPage />,
  },
  {
    path: "/calendar/:username",
    element: <CalendarPage />,
  },
]);
