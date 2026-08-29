"use client";

import { motion } from "framer-motion";
import { Home } from "lucide-react";
import { ConversationStarters } from "./ConversationStarters";

interface EmptyStateProps {
  onSelectStarter: (text: string) => void;
}

export function EmptyState({ onSelectStarter }: EmptyStateProps) {
  return (
    <div className="flex h-full flex-col items-center justify-center gap-8 px-6 py-16 text-center">
      <motion.div
        initial={{ opacity: 0, y: 12 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5, ease: "easeOut" }}
        className="flex flex-col items-center gap-4"
      >
        <span className="flex h-12 w-12 items-center justify-center rounded-full bg-[color:var(--accent-gold)]">
          <Home className="h-5 w-5 text-background" strokeWidth={2.5} />
        </span>

        <div className="max-w-md">
          <h1 className="font-serif text-2xl font-medium tracking-tight text-foreground md:text-3xl">
            👋 Hi, I&apos;m Shelby.
          </h1>
          <p className="mt-1 font-serif text-2xl font-medium tracking-tight text-foreground md:text-3xl">
            Tell me where you&apos;d like to move.
          </p>
          <p className="mt-4 leading-relaxed text-muted-foreground">
            I&apos;ll compare listings, neighborhoods and commute options to
            help you find your next home.
          </p>
        </div>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 12 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5, delay: 0.15, ease: "easeOut" }}
        className="flex w-full justify-center"
      >
        <ConversationStarters onSelect={onSelectStarter} />
      </motion.div>
    </div>
  );
}
