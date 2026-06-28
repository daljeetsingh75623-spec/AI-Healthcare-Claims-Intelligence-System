import { createBrowserRouter } from "react-router-dom";

import MainLayout from "../layouts/MainLayout";

import Dashboard from "../pages/Dashboard";
import Upload from "../pages/Upload";
import Claims from "../pages/Claims";
import Chat from "../pages/Chat";
import Analytics from "../pages/Analytics";
import Settings from "../pages/Settings";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <MainLayout />,
    children: [
      {
        index: true,
        element: <Dashboard />,
      },
      {
        path: "upload",
        element: <Upload />,
      },
      {
        path: "claims",
        element: <Claims />,
      },
      {
        path: "chat",
        element: <Chat />,
      },
      {
        path: "analytics",
        element: <Analytics />,
      },
      {
        path: "settings",
        element: <Settings />,
      },
    ],
  },
]);