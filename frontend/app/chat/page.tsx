"use client";

import { Suspense, useEffect, useState } from "react";
import { useSearchParams } from "next/navigation";
import { ChatLayout } from "@/components/chat/ChatLayout";
import { EmptyState } from "@/components/chat/EmptyState";
import { Conversation } from "@/components/chat/Conversation";
import { ChatInput } from "@/components/chat/ChatInput";
import type { Message } from "@/types/chat";

/**
 * DEMO ONLY: a single hardcoded reply used to showcase the UI states
 * (empty → user message → typing → reply). No backend, no LangChain,
 * no real understanding of the user's input — this is the exact slot
 * where a real API call will replace `simulateShelbyReply` later.
 */
function simulateShelbyReply(): string {
  return "Sure! What's your budget?";
}

function createMessage(role: Message["role"], content: string): Message {
  return {
    id: crypto.randomUUID(),
    role,
    content,
    createdAt: new Date().toISOString(),
  };
}

function ChatPageContent() {
  const searchParams = useSearchParams();
  const initialQuery = searchParams.get("q") ?? "";

  const [messages, setMessages] = useState<Message[]>(
    initialQuery ? [createMessage("user", initialQuery)] : []
  );
  const [inputValue, setInputValue] = useState("");
  const [isTyping, setIsTyping] = useState(Boolean(initialQuery));

  const respondAsShelby = () => {
    setIsTyping(true);
    // Placeholder timing for the demo checklist to play out fully.
    setTimeout(() => {
      setMessages((prev) => [...prev, createMessage("assistant", simulateShelbyReply())]);
      setIsTyping(false);
    }, 1800);
  };

  // Kick off the demo reply if the page opened with an initial query.
  useEffect(() => {
    if (initialQuery) respondAsShelby();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const handleSend = (text: string) => {
    const trimmed = text.trim();
    if (!trimmed) return;
    setMessages((prev) => [...prev, createMessage("user", trimmed)]);
    setInputValue("");
    respondAsShelby();
  };

  return (
    <ChatLayout
      input={
        <ChatInput
          value={inputValue}
          onChange={setInputValue}
          onSubmit={() => handleSend(inputValue)}
          disabled={isTyping}
        />
      }
    >
      {messages.length === 0 ? (
        <EmptyState onSelectStarter={(text) => setInputValue(text)} />
      ) : (
        <Conversation messages={messages} isTyping={isTyping} />
      )}
    </ChatLayout>
  );
}

export default function ChatPage() {
  return (
    <Suspense fallback={null}>
      <ChatPageContent />
    </Suspense>
  );
}
