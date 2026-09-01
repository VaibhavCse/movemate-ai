"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { motion } from "framer-motion";
import { Home } from "lucide-react";
import { FaGithub } from "react-icons/fa";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";

const NAV_LINKS = [
  { label: "Features", href: "#features" },
  { label: "How it Works", href: "#how-it-works" },
  { label: "GitHub", href: "https://github.com/VaibhavCse/movemate-ai", external: true },
];

export function Navbar() {
  const router = useRouter();
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 8);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <motion.header
      initial={{ y: -16, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.5, ease: "easeOut" }}
      className={cn(
        "fixed top-0 inset-x-0 z-50 transition-colors duration-300",
        scrolled
          ? "bg-background/80 backdrop-blur-md border-b border-border"
          : "bg-transparent border-b border-transparent"
      )}
    >
      <nav className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
        <a href="#top" className="flex items-center gap-2">
          <span className="flex h-8 w-8 items-center justify-center rounded-full bg-[color:var(--accent-gold)]">
            <Home className="h-4 w-4 text-background" strokeWidth={2.5} />
          </span>
          <span className="font-serif text-lg font-medium tracking-tight text-foreground">
            MoveMate <span className="text-muted-foreground">AI</span>
          </span>
        </a>

        <div className="hidden items-center gap-8 md:flex">
          {NAV_LINKS.map((link) => (
            <a
              key={link.label}
              href={link.href}
              target={link.external ? "_blank" : undefined}
              rel={link.external ? "noreferrer" : undefined}
              className="flex items-center gap-1.5 font-mono text-[13px] uppercase tracking-wide text-muted-foreground transition-colors hover:text-foreground"
            >
              {link.label === "GitHub" && <FaGithub className="h-3.5 w-3.5" />}
              {link.label}
            </a>
          ))}
        </div>

        <Button
          size="sm"
          onClick={() => router.push("/chat")}
          className="rounded-full bg-foreground text-background hover:bg-foreground/90"
        >
          Get Started
        </Button>
      </nav>
    </motion.header>
  );
}
