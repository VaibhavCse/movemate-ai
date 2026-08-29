"use client";

import { motion } from "framer-motion";

const SUGGESTIONS = [
  "Need a flat near Bellandur under ₹25k",
  "Looking for a PG in Whitefield",
  "Find pet-friendly apartments",
  "Show homes similar to this",
];

interface SuggestionChipsProps {
  onSelect: (text: string) => void;
}

export function SuggestionChips({ onSelect }: SuggestionChipsProps) {
  return (
    <motion.div
      initial="hidden"
      whileInView="show"
      viewport={{ once: true, amount: 0.6 }}
      variants={{
        hidden: {},
        show: { transition: { staggerChildren: 0.06, delayChildren: 0.1 } },
      }}
      className="mt-5 flex flex-wrap items-center justify-center gap-2.5"
    >
      {SUGGESTIONS.map((text) => (
        <motion.button
          key={text}
          type="button"
          onClick={() => onSelect(text)}
          variants={{
            hidden: { opacity: 0, y: 8 },
            show: { opacity: 1, y: 0, transition: { duration: 0.4, ease: "easeOut" } },
          }}
          whileHover={{ y: -2 }}
          className="rounded-full border border-border bg-card px-4 py-2 text-sm text-muted-foreground transition-colors hover:border-[color:var(--accent-gold)]/50 hover:text-foreground"
        >
          {text}
        </motion.button>
      ))}
    </motion.div>
  );
}
