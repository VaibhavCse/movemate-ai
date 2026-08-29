import { Home } from "lucide-react";
import { Separator } from "@/components/ui/separator";

export function Footer() {
  return (
    <footer className="px-6 py-10">
      <div className="mx-auto max-w-6xl">
        <Separator className="mb-8 bg-border" />
        <div className="flex flex-col items-center justify-between gap-4 md:flex-row">
          <div className="flex items-center gap-2">
            <span className="flex h-6 w-6 items-center justify-center rounded-full bg-[color:var(--accent-gold)]">
              <Home className="h-3.5 w-3.5 text-background" strokeWidth={2.5} />
            </span>
            <span className="font-serif text-sm font-medium text-foreground">
              MoveMate AI
            </span>
          </div>
          <p className="font-mono text-[12px] text-muted-foreground">
            © {new Date().getFullYear()} MoveMate AI. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
}
