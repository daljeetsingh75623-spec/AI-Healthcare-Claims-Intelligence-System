import type{ ReactNode } from "react";
import { motion } from "framer-motion";

interface PageHeaderProps {
  title: string;
  description: string;
  action?: ReactNode;
}

export default function PageHeader({
  title,
  description,
  action,
}: PageHeaderProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: -15 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.35 }}
      className="mb-8 flex flex-col gap-4 md:flex-row md:items-center md:justify-between"
    >
      <div>
        <h1 className="text-4xl font-bold tracking-tight text-slate-900">
          {title}
        </h1>

        <p className="mt-2 text-slate-500">
          {description}
        </p>
      </div>

      {action}
    </motion.div>
  );
}