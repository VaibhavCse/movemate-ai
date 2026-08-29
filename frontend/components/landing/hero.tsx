"use client";

import { motion } from "framer-motion";
import { Sparkles } from "lucide-react";
import { RooftopDivider } from "./rooftop-divider";

const container = {
  hidden: {},
  show: {
    transition: { staggerChildren: 0.09, delayChildren: 0.1 },
  },
};

const item = {
  hidden: { opacity: 0, y: 14 },
  show: { opacity: 1, y: 0, transition: { duration: 0.6, ease: "easeOut" } },
};

export function Hero() {
  return (
    <section id="top" className="relative overflow-hidden pt-40 pb-20 md:pt-48 md:pb-28">
      {/* Ambient glow behind the headline — the one intentional flourish */}
      <div
        aria-hidden="true"
        className="pointer-events-none absolute left-1/2 top-24 h-[420px] w-[720px] -translate-x-1/2 rounded-full opacity-[0.18] blur-3xl"
        style={{
          background:
            "radial-gradient(closest-side, var(--accent-gold), transparent)",
        }}
      />

      <motion.div
        variants={container}
        initial="hidden"
        animate="show"
        className="relative mx-auto flex max-w-3xl flex-col items-center px-6 text-center"
      >
        <motion.span
          variants={item}
          className="mb-6 inline-flex items-center gap-2 rounded-full border border-border bg-card px-3 py-1 font-mono text-[12px] uppercase tracking-wide text-muted-foreground"
        >
          <Sparkles className="h-3 w-3 text-[color:var(--accent-gold)]" />
          Introducing Shelby, your AI relocation assistant
        </motion.span>

        <motion.h1
          variants={item}
          className="font-serif text-5xl font-medium leading-[1.08] tracking-tight text-foreground md:text-6xl"
        >
          Find your next home
          <br />
          with AI, not endless scrolling.
        </motion.h1>

        <motion.p
          variants={item}
          className="mt-6 max-w-xl text-balance text-lg leading-relaxed text-muted-foreground"
        >
          Hi, I&apos;m Shelby. I&apos;ll compare listings, understand
          neighborhoods, and help you find your next home — no filters, no
          endless tabs.
        </motion.p>
      </motion.div>

      <div className="pointer-events-none absolute inset-x-0 bottom-0 text-border">
        <RooftopDivider className="h-16 md:h-24" />
      </div>
    </section>
  );
}
