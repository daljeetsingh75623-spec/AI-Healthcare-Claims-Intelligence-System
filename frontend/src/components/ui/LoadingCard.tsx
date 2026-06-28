import { Skeleton } from "@/components/ui/skeleton";

export default function LoadingCard() {
  return (
    <div className="space-y-3 rounded-2xl border bg-white p-6">

      <Skeleton className="h-5 w-36" />

      <Skeleton className="h-10 w-28" />

      <Skeleton className="h-4 w-full" />

    </div>
  );
}