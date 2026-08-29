# ADR-002: Session Memory for MVP

Status: Accepted

Date: 2026-07-21

---

## Context

Users expect Shelby to remember information during a conversation.

However, implementing permanent memory requires authentication, databases, and privacy considerations.

---

## Decision

Version 1 will use **session memory only**.

Shelby remembers information only during the active conversation.

---

## Consequences

Advantages

- Simple implementation
- Faster responses
- No authentication required
- Better privacy for MVP

Future versions may introduce persistent memory tied to user accounts.