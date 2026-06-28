import type{ ReactNode } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { motion } from "framer-motion";

interface StatCardProps {
  title: string;
  value: string;
  change: string;
  icon: ReactNode;
}

export default function StatCard({
  title,
  value,
  change,
  icon,
}: StatCardProps) {
  return (
    <motion.div
      whileHover={{
        y: -6,
        scale: 1.02,
      }}
      transition={{
        duration: 0.2,
      }}
    >
      <Card className="rounded-2xl border-0 shadow-md hover:shadow-xl">

        <CardContent className="flex items-center justify-between p-6">

          <div>

            <p className="text-sm text-slate-500">
              {title}
            </p>

            <h2 className="mt-3 text-3xl font-bold">
              {value}
            </h2>

            <p className="mt-2 text-sm font-medium text-emerald-600">
              {change}
            </p>

          </div>

          <div className="rounded-2xl bg-blue-50 p-4">
            {icon}
          </div>

        </CardContent>

      </Card>
    </motion.div>
  );
}