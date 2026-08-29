"use client";

import { motion } from "framer-motion";
import { Home, User } from "lucide-react";
import { cn } from "@/lib/utils";
import type { Message } from "@/types/chat";

interface ChatMessageProps {
  message: Message;
}

export function ChatMessage({ message }: ChatMessageProps) {
  const isUser = message.role === "user";

  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, ease: "easeOut" }}
      className={cn("flex items-start gap-3", isUser && "flex-row-reverse")}
    >
      <span
        className={cn(
          "flex h-8 w-8 shrink-0 items-center justify-center rounded-full",
          isUser
            ? "bg-muted text-muted-foreground"
            : "bg-[color:var(--accent-gold)] text-background"
        )}
      >
        {isUser ? (
          <User className="h-4 w-4" strokeWidth={2} />
        ) : (
          <Home className="h-4 w-4" strokeWidth={2.5} />
        )}
      </span>

      <div
        className={cn(
          "max-w-[75%] rounded-2xl px-4 py-2.5 text-[15px] leading-relaxed",
          isUser
            ? "rounded-tr-sm bg-foreground text-background"
            : "rounded-tl-sm border border-border bg-card text-foreground"
        )}
      >
        {message.content}
      </div>
    </motion.div>
  );
}
