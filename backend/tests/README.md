# MoveMate AI Tests

This directory contains all automated tests for the backend.

## Test Categories

### Unit Tests

Tests individual modules in isolation.

Examples

- Memory Manager
- Decision Engine
- Intent Detector

---

### Integration Tests

Tests communication between modules.

Examples

- Conversation Manager → Decision Engine
- Decision Engine → Tool Manager

---

### API Tests

Tests FastAPI endpoints.

Examples

- POST /chat
- Error responses
- Invalid requests

---

### Future Tests

- LLM integration
- Tavily integration
- Cache validation
- Performance testing

## Goal

Every backend module should have corresponding automated tests.