# MoveMate AI Backend

The backend powers Shelby, the AI relocation assistant.

## Responsibilities

- Conversation Management
- Session Memory
- Decision Engine
- Search Planning
- AI Orchestration
- Response Formatting

## Tech Stack

- FastAPI
- Python
- Pydantic
- Gemini
- Tavily

## Architecture

Conversation Manager

↓

Intent Detector

↓

Change Detector

↓

Decision Engine

↓

Search Strategy Engine

↓

Cache Manager

↓

Tool Manager

↓

LLM Service

↓

Response Builder

## Design Principles

- Single Responsibility
- Modular Design
- Provider Independent
- Test Driven
- AI as a Service