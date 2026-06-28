import { motion } from "framer-motion";

export default function WelcomeBanner() {
  return (
    <motion.div
      initial={{ opacity: 0, y: -20 }}
      animate={{ opacity: 1, y: 0 }}
      className="rounded-2xl bg-gradient-to-r from-blue-600 to-cyan-500 p-8 text-white"
    >
      <h1 className="text-4xl font-bold">
        Welcome Back 👋
      </h1>

      <p className="mt-2 text-blue-100">
        AI Healthcare Claims Intelligence System
      </p>
    </motion.div>
  );
}