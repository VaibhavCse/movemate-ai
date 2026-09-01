"use client";

import { Suspense, useEffect, useRef, useState } from "react";
import { useSearchParams } from "next/navigation";
import { ChatLayout } from "@/components/chat/ChatLayout";
import { EmptyState } from "@/components/chat/EmptyState";
import { Conversation } from "@/components/chat/Conversation";
import { ChatInput } from "@/components/chat/ChatInput";
import type { Message } from "@/types/chat";

const API_URL =
  process.env.NEXT_PUBLIC_API_URL ?? "http://127.0.0.1:8000/api/v1";

interface ChatResponse {
  reply: string;
  session_id: string | null;
}

function createMessage(
  role: Message["role"],
  content: string,
  status: Message["status"] = "sent",
): Message {
  return {
    id: crypto.randomUUID(),
    role,
    content,
    createdAt: new Date().toISOString(),
    status,
  };
}

function ChatPageContent() {
  const searchParams = useSearchParams();
  const initialQuery = searchParams.get("q") ?? "";

  const [messages, setMessages] = useState<Message[]>([]);
  const [inputValue, setInputValue] = useState("");
  const [isTyping, setIsTyping] = useState(false);
  const [sessionId, setSessionId] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const initialQueryHandled = useRef(false);

  const sendMessage = async (text: string) => {
    const trimmed = text.trim();

    if (!trimmed || isTyping) {
      return;
    }

    setError(null);
    setInputValue("");

    const userMessage = createMessage("user", trimmed);

    setMessages((prev) => [...prev, userMessage]);
    setIsTyping(true);

    try {
      const response = await fetch(`${API_URL}/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: trimmed,
          ...(sessionId ? { session_id: sessionId } : {}),
        }),
      });

      if (!response.ok) {
        const errorText = await response.text();

        console.error("Backend error:", {
          status: response.status,
          body: errorText,
        });

        throw new Error(`Backend returned ${response.status}`);
      }

      const data: ChatResponse = await response.json();

      if (!data.reply) {
        throw new Error("Backend returned an empty reply.");
      }

      if (data.session_id) {
        setSessionId(data.session_id);
      }

      const assistantMessage = createMessage(
        "assistant",
        data.reply,
      );

      setMessages((prev) => [
        ...prev,
        assistantMessage,
      ]);
    } catch (err) {
      console.error("Chat request failed:", err);

      setError(
        "Shelby is temporarily unavailable. Please check that the backend is running and try again.",
      );

      const errorMessage = createMessage(
        "assistant",
        "Sorry, I couldn't reach Shelby right now. Please try again.",
        "error",
      );

      setMessages((prev) => [
        ...prev,
        errorMessage,
      ]);
    } finally {
      setIsTyping(false);
    }
  };

  useEffect(() => {
    if (
      !initialQuery ||
      initialQueryHandled.current
    ) {
      return;
    }

    initialQueryHandled.current = true;

    sendMessage(initialQuery);
  }, [initialQuery]);

  const handleSend = (text: string) => {
    sendMessage(text);
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
        <EmptyState
          onSelectStarter={(text) =>
            setInputValue(text)
          }
        />
      ) : (
        <Conversation
          messages={messages}
          isTyping={isTyping}
        />
      )}

      {error && (
        <div className="mx-auto w-full max-w-2xl px-6 pb-3 text-sm text-destructive">
          {error}
        </div>
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