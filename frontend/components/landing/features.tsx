"use client";

import { motion } from "framer-motion";
import { Sparkles, SearchCheck, MapPinned } from "lucide-react";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
} from "@/components/ui/card";

const FEATURES = [
  {
    icon: Sparkles,
    title: "AI Recommendations",
    description:
      "Shelby learns what you actually care about — commute, budget, vibe — and narrows thousands of listings down to the ones worth your time.",
  },
  {
    icon: SearchCheck,
    title: "Live Property Search",
    description:
      "Search in plain language instead of stacking filters. Shelby reads the request and pulls matching homes as you describe them.",
  },
  {
    icon: MapPinned,
    title: "Neighborhood Insights",
    description:
      "Get a real feel for an area — walkability, noise, nearby essentials — before you spend a weekend visiting it in person.",
  },
];

export function Features() {
  return (
    <section id="features" className="px-6 py-24 md:py-32">
      <div className="mx-auto max-w-6xl">
        <motion.div
          initial={{ opacity: 0, y: 12 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.5 }}
          transition={{ duration: 0.5 }}
          className="mx-auto mb-14 max-w-xl text-center"
        >
          <span className="font-mono text-[12px] uppercase tracking-wide text-muted-foreground">
            Why MoveMate
          </span>
          <h2 className="mt-3 font-serif text-3xl font-medium tracking-tight text-foreground md:text-4xl">
            A calmer way to house-hunt
          </h2>
        </motion.div>

        <div className="grid gap-6 md:grid-cols-3">
          {FEATURES.map((feature, i) => (
            <motion.div
              key={feature.title}
              initial={{ opacity: 0, y: 16 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.4 }}
              transition={{ duration: 0.5, delay: i * 0.08 }}
              whileHover={{ y: -4 }}
            >
              <Card className="h-full rounded-2xl border-border bg-card p-2 shadow-none transition-shadow hover:shadow-[0_16px_40px_-20px_rgba(20,21,26,0.18)]">
                <CardHeader className="gap-4">
                  <div className="flex h-11 w-11 items-center justify-center rounded-xl bg-[color:var(--accent-sage)]/12">
                    <feature.icon
                      className="h-5 w-5 text-[color:var(--accent-sage)]"
                      strokeWidth={1.75}
                    />
                  </div>
                  <CardTitle className="font-serif text-xl font-medium tracking-tight">
                    {feature.title}
                  </CardTitle>
                  <CardDescription className="leading-relaxed">
                    {feature.description}
                  </CardDescription>
                </CardHeader>
              </Card>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
