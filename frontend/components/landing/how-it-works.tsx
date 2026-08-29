"use client";

import { motion } from "framer-motion";
import { MessageSquareText, ListFilter, Sparkle } from "lucide-react";

const STEPS = [
  {
    icon: MessageSquareText,
    title: "Tell Shelby your requirements",
    description:
      "Describe your budget, area, and must-haves in your own words — the way you'd explain it to a friend.",
  },
  {
    icon: ListFilter,
    title: "Shelby searches and compares",
    description:
      "Shelby sifts through listings and neighborhoods, weighing the details that matter to your specific search.",
  },
  {
    icon: Sparkle,
    title: "Receive personalized recommendations",
    description:
      "Get a short, curated list of homes worth seeing — with the reasoning behind each one.",
  },
];

export function HowItWorks() {
  return (
    <section id="how-it-works" className="border-t border-border px-6 py-24 md:py-32">
      <div className="mx-auto max-w-4xl">
        <motion.div
          initial={{ opacity: 0, y: 12 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.5 }}
          transition={{ duration: 0.5 }}
          className="mb-16 text-center"
        >
          <span className="font-mono text-[12px] uppercase tracking-wide text-muted-foreground">
            How it works
          </span>
          <h2 className="mt-3 font-serif text-3xl font-medium tracking-tight text-foreground md:text-4xl">
            Three steps, no scrolling
          </h2>
        </motion.div>

        <div className="relative flex flex-col gap-10 md:gap-0">
          {/* Connecting line — encodes that this genuinely is a sequence */}
          <div
            aria-hidden="true"
            className="absolute left-6 top-2 hidden h-[calc(100%-2.5rem)] w-px bg-border md:block"
          />

          {STEPS.map((step, i) => (
            <motion.div
              key={step.title}
              initial={{ opacity: 0, x: -14 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true, amount: 0.5 }}
              transition={{ duration: 0.5, delay: i * 0.1 }}
              className="relative flex items-start gap-5 py-5 md:py-8"
            >
              <span className="relative z-10 flex h-12 w-12 shrink-0 items-center justify-center rounded-full border border-border bg-background">
                <step.icon
                  className="h-5 w-5 text-[color:var(--accent-gold)]"
                  strokeWidth={1.75}
                />
              </span>
              <div className="pt-1.5">
                <h3 className="font-serif text-xl font-medium tracking-tight text-foreground">
                  {step.title}
                </h3>
                <p className="mt-1.5 max-w-md leading-relaxed text-muted-foreground">
                  {step.description}
                </p>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
