# ADR-003: Provider Independent LLM Layer

Status: Accepted

Date: 2026-07-21

---

## Context

AI providers evolve rapidly.

The application should not depend directly on Gemini APIs.

---

## Decision

Introduce an LLM Service layer.

All backend modules communicate only with LLMService.

LLMService internally communicates with Gemini.

Future providers such as OpenAI, Claude, or DeepSeek can be added without changing the application architecture.

---

## Consequences

Advantages

- Easy provider switching
- Cleaner architecture
- Better testing
- Reduced vendor lock-in