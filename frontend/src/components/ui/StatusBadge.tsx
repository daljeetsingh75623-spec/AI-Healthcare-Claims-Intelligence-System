import { Badge } from "@/components/ui/badge";

interface Props {
  status: "success" | "warning" | "error" | "processing";
}

export default function StatusBadge({ status }: Props) {
  const styles = {
    success: "bg-green-100 text-green-700",
    warning: "bg-yellow-100 text-yellow-700",
    error: "bg-red-100 text-red-700",
    processing: "bg-blue-100 text-blue-700",
  };

  return (
    <Badge className={styles[status]}>
      {status.toUpperCase()}
    </Badge>
  );
}