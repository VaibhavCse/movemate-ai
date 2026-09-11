"use client";

import { KeyboardEvent, useState } from "react";
import { useRouter } from "next/navigation";
import { motion } from "framer-motion";
import { ArrowUp } from "lucide-react";
import { Input } from "@/components/ui/input";
import { SuggestionChips } from "./suggestion-chips";

export function ConversationalSearch() {
  const router = useRouter();
  const [value, setValue] = useState("");

  const goToChat = (text: string) => {
    const trimmed = text.trim();
    const query = trimmed ? `?q=${encodeURIComponent(trimmed)}` : "";
    router.push(`/chat${query}`);
  };

  const handleKeyDown = (event: KeyboardEvent<HTMLInputElement>) => {
    if (event.key === "Enter") {
      event.preventDefault();
      goToChat(value);
    }
  };

  return (
    <section className="relative px-6 pb-24 md:pb-32">
      <motion.div
        initial={{ opacity: 0, y: 18 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.4 }}
        transition={{ duration: 0.6, ease: "easeOut" }}
        className="mx-auto max-w-2xl"
      >
        <div className="flex items-center gap-2 rounded-2xl border border-border bg-card p-2.5 shadow-[0_1px_2px_rgba(20,21,26,0.04),0_12px_32px_-16px_rgba(20,21,26,0.12)] transition-shadow focus-within:shadow-[0_1px_2px_rgba(20,21,26,0.04),0_16px_40px_-14px_rgba(232,163,61,0.28)]">
          <Input
            value={value}
            onChange={(e) => setValue(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Ask Shelby where you'd like to live..."
            className="h-10 flex-1 border-0 bg-transparent px-1 text-base shadow-none focus-visible:ring-0"
          />

          <button
            type="button"
            aria-label="Send message"
            onClick={() => goToChat(value)}
            className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-foreground text-background transition-transform hover:scale-105"
          >
            <ArrowUp className="h-[18px] w-[18px]" />
          </button>
        </div>

        <SuggestionChips onSelect={goToChat} />
      </motion.div>
    </section>
  );
}