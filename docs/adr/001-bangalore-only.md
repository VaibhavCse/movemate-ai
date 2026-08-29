# ADR-001: Bangalore Only for MVP

Status: Accepted

Date: 2026-07-21

---

## Context

MoveMate AI aims to become an AI relocation assistant for India.

Supporting multiple cities in the MVP would significantly increase complexity, including:

- Area mapping
- Search quality
- Recommendation logic
- Testing effort
- API costs

---

## Decision

Version 1 of MoveMate AI will support **Bangalore only**.

If a user requests another city, Shelby will politely inform them that Bangalore is currently supported and that more cities are planned in future releases.

---

## Consequences

### Advantages

- Faster MVP delivery
- Better recommendation quality
- Easier testing
- Lower maintenance
- Reduced API usage

### Future

Multi-city support will be introduced after the Bangalore experience is stable.