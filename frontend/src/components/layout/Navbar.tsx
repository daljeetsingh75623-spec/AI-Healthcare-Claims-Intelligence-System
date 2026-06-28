import { Bell, Search, UserCircle2 } from "lucide-react";

export default function Navbar() {
  return (
    <header className="h-16 bg-white border-b border-slate-200 flex items-center justify-between px-8">

      <div className="relative w-96">

        <Search
          className="absolute left-3 top-3 text-slate-400"
          size={18}
        />

        <input
          type="text"
          placeholder="Search claims, policies..."
          className="w-full rounded-xl border border-slate-300 py-2 pl-10 pr-4 outline-none focus:ring-2 focus:ring-blue-500"
        />

      </div>

      <div className="flex items-center gap-6">

        <Bell
          className="cursor-pointer text-slate-600"
          size={22}
        />

        <div className="flex items-center gap-3">

          <UserCircle2
            size={36}
            className="text-blue-600"
          />

          <div>
            <h2 className="font-semibold">
              Daljeet Singh
            </h2>

            <p className="text-xs text-slate-500">
              AI Engineer
            </p>
          </div>

        </div>

      </div>

    </header>
  );
}