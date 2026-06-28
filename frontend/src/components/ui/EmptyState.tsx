import { Inbox } from "lucide-react";

interface Props {
  title: string;
  description: string;
}

export default function EmptyState({
  title,
  description,
}: Props) {
  return (
    <div className="flex flex-col items-center justify-center rounded-2xl border-2 border-dashed border-slate-300 p-12 text-center">

      <Inbox className="mb-4 text-slate-400" size={50} />

      <h2 className="text-xl font-semibold">
        {title}
      </h2>

      <p className="mt-2 text-slate-500">
        {description}
      </p>

    </div>
  );
}