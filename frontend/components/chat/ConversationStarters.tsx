"use client";

import { motion } from "framer-motion";

interface Starter {
  emoji: string;
  text: string;
}

const STARTERS: Starter[] = [
  { emoji: "🏠", text: "Need a flat near Bellandur under ₹25k" },
  { emoji: "🏢", text: "Looking for a PG in Whitefield" },
  { emoji: "🐶", text: "Find pet-friendly apartments" },
  { emoji: "📷", text: "Find homes similar to this" },
];

interface ConversationStartersProps {
  onSelect: (text: string) => void;
}

export function ConversationStarters({ onSelect }: ConversationStartersProps) {
  return (
    <motion.div
      initial="hidden"
      animate="show"
      variants={{
        hidden: {},
        show: { transition: { staggerChildren: 0.07, delayChildren: 0.2 } },
      }}
      className="grid w-full max-w-xl grid-cols-1 gap-2.5 sm:grid-cols-2"
    >
      {STARTERS.map((starter) => (
        <motion.button
          key={starter.text}
          type="button"
          onClick={() => onSelect(starter.text)}
          variants={{
            hidden: { opacity: 0, y: 10 },
            show: { opacity: 1, y: 0, transition: { duration: 0.4, ease: "easeOut" } },
          }}
          whileHover={{ y: -2 }}
          className="flex items-start gap-2.5 rounded-2xl border border-border bg-card px-4 py-3 text-left text-sm text-muted-foreground transition-colors hover:border-[color:var(--accent-gold)]/50 hover:text-foreground"
        >
          <span aria-hidden="true" className="text-base leading-none">
            {starter.emoji}
          </span>
          <span className="leading-snug">{starter.text}</span>
        </motion.button>
      ))}
    </motion.div>
  );
}
