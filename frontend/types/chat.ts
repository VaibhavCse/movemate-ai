/**
 * Core chat types for MoveMate AI.
 *
 * These are intentionally decoupled from any transport or backend shape.
 * When the LangChain/API layer is introduced, these interfaces should only
 * need new optional fields (e.g. `sources`, `toolCalls`), not breaking changes.
 */

export type Role = "user" | "assistant" | "system";

export type AttachmentType = "image" | "file";

export interface Attachment {
  id: string;
  type: AttachmentType;
  url: string;
  name?: string;
}

export type MessageStatus = "sending" | "sent" | "error";

export interface Message {
  id: string;
  role: Role;
  content: string;
  createdAt: string; // ISO timestamp
  attachments?: Attachment[];
  /** Present once streaming/error states exist; absent for static/demo messages. */
  status?: MessageStatus;
}

export interface Conversation {
  id: string;
  title?: string;
  messages: Message[];
  createdAt: string;
  updatedAt: string;
}

/** A single step in Shelby's "thinking" sequence, shown in TypingIndicator. */
export interface ThinkingStep {
  id: string;
  label: string;
  done: boolean;
}
