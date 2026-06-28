import { Card, CardContent } from "@/components/ui/card";
import { motion } from "framer-motion";

interface MetricCardProps {
  title: string;
  value: string;
  change: string;
  icon: React.ElementType;
  color: string;
}

export default function MetricCard({
  title,
  value,
  change,
  icon: Icon,
  color,
}: MetricCardProps) {
  return (
    <motion.div
      whileHover={{ y: -5 }}
      transition={{ duration: 0.2 }}
    >
      <Card className="rounded-2xl shadow-md hover:shadow-xl transition-all">
        <CardContent className="p-6">

          <div className="flex items-center justify-between">

            <div>

              <p className="text-sm text-slate-500">
                {title}
              </p>

              <h2 className="mt-2 text-3xl font-bold">
                {value}
              </h2>

              <p className="mt-2 text-sm text-emerald-600">
                {change}
              </p>

            </div>

            <Icon
              className={color}
              size={38}
            />

          </div>

        </CardContent>
      </Card>
    </motion.div>
  );
}