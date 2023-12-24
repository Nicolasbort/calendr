import CalendarPage from "pages/CalendarPage";
import HomePage from "pages/HomePage";
import PatientDetailsPage from "pages/PatientDetailsPage";
import SearchPage from "pages/SearchPage";
import { createBrowserRouter } from "react-router-dom";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <HomePage />,
  },
  {
    path: "/patients",
    element: <SearchPage />,
  },
  {
    path: "/patients/:id",
    element: <PatientDetailsPage />,
  },
  {
    path: "/calendar/:username",
    element: <CalendarPage />,
  },
]);
