import {
  FileText,
  ShieldAlert,
  ShieldCheck,
  Brain,
} from "lucide-react";

export const dashboardStats = [
  {
    title: "Claims Processed",
    value: "1,284",
    change: "+12%",
    icon: FileText,
    color: "text-blue-600",
  },
  {
    title: "Fraud Alerts",
    value: "18",
    change: "-4%",
    icon: ShieldAlert,
    color: "text-red-500",
  },
  {
    title: "Policies Uploaded",
    value: "436",
    change: "+8%",
    icon: ShieldCheck,
    color: "text-emerald-600",
  },
  {
    title: "AI Accuracy",
    value: "98.4%",
    change: "+0.6%",
    icon: Brain,
    color: "text-purple-600",
  },
];