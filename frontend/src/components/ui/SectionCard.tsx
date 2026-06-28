import type{ ReactNode } from "react";
import { Card, CardContent } from "@/components/ui/card";

interface SectionCardProps {
  title: string;
  children: ReactNode;
}

export default function SectionCard({
  title,
  children,
}: SectionCardProps) {
  return (
    <Card className="rounded-2xl shadow-sm border-0">
      <CardContent className="p-6">

        <h2 className="mb-6 text-xl font-semibold">
          {title}
        </h2>

        {children}

      </CardContent>
    </Card>
  );
}