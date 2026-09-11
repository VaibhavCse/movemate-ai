"use client";

import { KeyboardEvent } from "react";
import { ArrowUp } from "lucide-react";
import { Input } from "@/components/ui/input";

interface ChatInputProps {
  value: string;
  onChange: (value: string) => void;
  onSubmit: () => void;
  disabled?: boolean;
}

export function ChatInput({
  value,
  onChange,
  onSubmit,
  disabled = false,
}: ChatInputProps) {
  const canSend = value.trim().length > 0 && !disabled;

  const handleKeyDown = (event: KeyboardEvent<HTMLInputElement>) => {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();

      if (canSend) {
        onSubmit();
      }
    }
  };

  return (
    <div className="mx-auto w-full max-w-2xl px-6 py-4">
      <div className="flex items-center gap-2 rounded-2xl border border-border bg-card p-2.5 shadow-[0_1px_2px_rgba(20,21,26,0.04),0_12px_32px_-16px_rgba(20,21,26,0.12)] transition-shadow focus-within:shadow-[0_1px_2px_rgba(20,21,26,0.04),0_16px_40px_-14px_rgba(232,163,61,0.28)]">
        <Input
          value={value}
          onChange={(e) => onChange(e.target.value)}
          onKeyDown={handleKeyDown}
          disabled={disabled}
          placeholder="Ask Shelby where you'd like to live..."
          className="h-10 flex-1 border-0 bg-transparent px-1 text-base shadow-none focus-visible:ring-0"
        />

        <button
          type="button"
          aria-label="Send message"
          onClick={onSubmit}
          disabled={!canSend}
          className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-foreground text-background transition-transform hover:scale-105 disabled:pointer-events-none disabled:opacity-40"
        >
          <ArrowUp className="h-[18px] w-[18px]" />
        </button>
      </div>
    </div>
  );
}