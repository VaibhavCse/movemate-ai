"use client";

import { useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Check, Loader2, Home } from "lucide-react";
import { cn } from "@/lib/utils";
import type { ThinkingStep } from "@/types/chat";

const INITIAL_STEPS: ThinkingStep[] = [
  { id: "understand", label: "Understanding requirements", done: false },
  { id: "search", label: "Searching listings", done: false },
  { id: "compare", label: "Comparing properties", done: false },
  { id: "rank", label: "Ranking recommendations", done: false },
];

/** How long each step stays "in progress" before completing, in ms. */
const STEP_INTERVAL = 420;

export function TypingIndicator() {
  const [steps, setSteps] = useState<ThinkingStep[]>(INITIAL_STEPS);

  useEffect(() => {
    let index = 0;
    const timer = setInterval(() => {
      setSteps((prev) => {
        if (index >= prev.length) {
          clearInterval(timer);
          return prev;
        }
        const next = prev.map((step, i) => (i === index ? { ...step, done: true } : step));
        index += 1;
        return next;
      });
    }, STEP_INTERVAL);

    return () => clearInterval(timer);
  }, []);

  const activeIndex = steps.findIndex((s) => !s.done);

  return (
    <motion.div
      initial={{ opacity: 0, y: 8 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -8 }}
      className="flex items-start gap-3"
    >
      <span className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-[color:var(--accent-gold)] text-background">
        <Home className="h-4 w-4" strokeWidth={2.5} />
      </span>

      <div className="min-w-[220px] rounded-2xl rounded-tl-sm border border-border bg-card px-4 py-3">
        <p className="mb-2 font-mono text-[12px] uppercase tracking-wide text-muted-foreground">
          Shelby is thinking
          <motion.span
            aria-hidden="true"
            animate={{ opacity: [0.2, 1, 0.2] }}
            transition={{ duration: 1.2, repeat: Infinity, ease: "easeInOut" }}
          >
            ...
          </motion.span>
        </p>

        <ul className="flex flex-col gap-1.5">
          <AnimatePresence initial={false}>
            {steps.map((step, i) => {
              const isActive = i === activeIndex;
              const isPending = i > activeIndex && activeIndex !== -1;

              return (
                <motion.li
                  key={step.id}
                  initial={{ opacity: 0, x: -6 }}
                  animate={{ opacity: isPending ? 0.4 : 1, x: 0 }}
                  transition={{ duration: 0.3 }}
                  className={cn(
                    "flex items-center gap-2 text-sm",
                    step.done ? "text-foreground" : "text-muted-foreground"
                  )}
                >
                  {step.done ? (
                    <Check className="h-3.5 w-3.5 shrink-0 text-[color:var(--accent-sage)]" />
                  ) : isActive ? (
                    <Loader2 className="h-3.5 w-3.5 shrink-0 animate-spin" />
                  ) : (
                    <span className="h-3.5 w-3.5 shrink-0 rounded-full border border-border" />
                  )}
                  {step.label}
                </motion.li>
              );
            })}
          </AnimatePresence>
        </ul>
      </div>
    </motion.div>
  );
}
