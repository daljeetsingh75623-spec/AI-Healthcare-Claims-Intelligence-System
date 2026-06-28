import { NavLink } from "react-router-dom";
import {
  LayoutDashboard,
  Upload,
  FileText,
  MessageSquare,
  BarChart3,
  Settings,
  ShieldPlus,
} from "lucide-react";

const menuItems = [
  {
    name: "Dashboard",
    path: "/",
    icon: LayoutDashboard,
  },
  {
    name: "Upload",
    path: "/upload",
    icon: Upload,
  },
  {
    name: "Claims",
    path: "/claims",
    icon: FileText,
  },
  {
    name: "AI Chat",
    path: "/chat",
    icon: MessageSquare,
  },
  {
    name: "Analytics",
    path: "/analytics",
    icon: BarChart3,
  },
  {
    name: "Settings",
    path: "/settings",
    icon: Settings,
  },
];

export default function Sidebar() {
  return (
    <aside className="w-72 bg-white border-r border-slate-200 flex flex-col">

      <div className="flex items-center gap-3 p-6 border-b border-slate-200">

        <ShieldPlus className="text-blue-600" size={34} />

        <div>
          <h1 className="font-bold text-lg">
            HealthClaims AI
          </h1>

          <p className="text-xs text-slate-500">
            Intelligence Platform
          </p>
        </div>

      </div>

      <nav className="flex-1 px-4 py-6">

        {menuItems.map((item) => {

          const Icon = item.icon;

          return (
            <NavLink
              key={item.path}
              to={item.path}
              className={({ isActive }) =>
                `flex items-center gap-3 rounded-xl px-4 py-3 mb-2 transition-all duration-300
                ${
                  isActive
                    ? "bg-blue-600 text-white shadow-lg"
                    : "text-slate-600 hover:bg-slate-100"
                }`
              }
            >
              <Icon size={20} />

              {item.name}
            </NavLink>
          );
        })}

      </nav>

    </aside>
  );
}