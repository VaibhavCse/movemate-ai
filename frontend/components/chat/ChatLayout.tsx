"use client";

import { ReactNode } from "react";
import Link from "next/link";
import { ArrowLeft, Home } from "lucide-react";

interface ChatLayoutProps {
  children: ReactNode;
  input: ReactNode;
}

export function ChatLayout({ children, input }: ChatLayoutProps) {
  return (
    <div className="flex h-dvh flex-col bg-background">
      <header className="flex shrink-0 items-center justify-between border-b border-border px-6 py-3.5">
        <Link
          href="/"
          className="flex items-center gap-2 text-muted-foreground transition-colors hover:text-foreground"
        >
          <ArrowLeft className="h-4 w-4" />
          <span className="font-mono text-[12px] uppercase tracking-wide">Home</span>
        </Link>

        <div className="flex items-center gap-2">
          <span className="flex h-6 w-6 items-center justify-center rounded-full bg-[color:var(--accent-gold)]">
            <Home className="h-3.5 w-3.5 text-background" strokeWidth={2.5} />
          </span>
          <span className="font-serif text-sm font-medium tracking-tight text-foreground">
            MoveMate <span className="text-muted-foreground">AI</span>
          </span>
        </div>

        {/* Right-side spacer keeps the logo visually centered against the back link */}
        <div className="w-[68px]" aria-hidden="true" />
      </header>

      <div className="flex-1 overflow-y-auto">{children}</div>

      <div className="shrink-0 border-t border-border bg-background/80 backdrop-blur-md">
        {input}
      </div>
    </div>
  );
}
