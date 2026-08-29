# ADR-004: Single Chat Endpoint

Status: Accepted

Date: 2026-07-21

---

## Context

Many AI applications expose multiple endpoints for different actions.

This increases frontend complexity.

---

## Decision

Version 1 will expose a single endpoint.

POST /chat

The backend will determine the required action.

---

## Consequences

Advantages

- Simpler frontend
- Cleaner API
- Easier maintenance
- Future extensibility