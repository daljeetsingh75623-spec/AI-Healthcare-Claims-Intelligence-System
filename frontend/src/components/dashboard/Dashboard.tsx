import WelcomeBanner from "@/components/dashboard/WelcomeBanner";
import MetricCard from "@/components/dashboard/MetricCard";

import { dashboardStats } from "@/data/dashboard";

export default function Dashboard() {
  return (
    <div className="space-y-8">

      <WelcomeBanner />

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

        {dashboardStats.map((item) => (
          <MetricCard
            key={item.title}
            {...item}
          />
        ))}

      </div>

    </div>
  );
}