# MoveMate AI - AI Architecture

Version: 1.0

Status: Approved

---

# Purpose

This document defines how the AI system inside MoveMate AI works.

The goal of this architecture is to build an AI assistant that behaves like a real relocation consultant instead of a simple chatbot.

The architecture is designed to be:

- Modular
- Scalable
- Provider Independent
- Cost Efficient
- Easy to maintain
- Optimized for Free Tier APIs

---

# Core Philosophy

Large Language Models should NOT control the application.

The backend controls the application.

The LLM only performs tasks where intelligence is required.

Examples:

✔ Natural language understanding

✔ Reasoning

✔ Ranking recommendations

✔ Explaining decisions

Everything else should be handled by our backend.

---

# High Level Architecture

                User
                  │
                  ▼
          Next.js Frontend
                  │
            POST /chat
                  │
                  ▼
            FastAPI Backend
                  │
                  ▼
      Conversation Manager
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
 Memory Manager      State Detector
        │                   │
        └─────────┬─────────┘
                  ▼
          Decision Engine
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
      Tool Manager      Response Builder
        │
        ▼
    Tavily Search
        │
        ▼
    LLM Service
        │
        ▼
 Gemini / OpenAI / Claude
        │
        ▼
 Structured Report
        │
        ▼
     Frontend

---

# Design Principle

Every module should have only ONE responsibility.

No file should try to perform multiple unrelated tasks.

---

# Backend Modules

## 1. Conversation Manager

Responsibility

Acts as the brain of every conversation.

Every user message enters through this module.

Responsibilities

• Receive user message

• Load conversation memory

• Update memory

• Call State Detector

• Decide next step

• Coordinate remaining modules

This module never performs AI reasoning.

It only controls workflow.

---

## 2. Memory Manager

Responsibility

Store everything Shelby learns during the session.

Examples

Budget

Area

Office Location

Property Type

Preferences

Memory exists only during the active session in Version 1.

Future versions may store persistent memory.

---

## 3. State Detector

Responsibility

Determine whether Shelby has enough information.

Examples

Need Flat

↓

Missing Budget

↓

Ask Budget

OR

Need Flat

Budget

Area

↓

Enough Information

↓

Proceed to Search

The State Detector never calls AI.

It simply checks conversation state.

---

## 4. Decision Engine

Responsibility

Decide what should happen next.

Possible actions

Ask Question

Search Listings

Generate Recommendation

Suggest Nearby Areas

Handle Errors

This module decides the workflow.

Not Gemini.

---

## 5. Tool Manager

Responsibility

Manage external tools.

Version 1

Tavily Search

Future

Google Maps

Weather

Travel Time

Rental APIs

Vector Database

The Conversation Manager never talks directly to tools.

Everything passes through Tool Manager.

---

## 6. LLM Service

Responsibility

Communicate with any language model.

Supported in future

Gemini

OpenAI

Claude

DeepSeek

The rest of the application should never know which provider is being used.

Only this service changes when switching providers.

---

## 7. Response Builder

Responsibility

Convert raw AI output into frontend-friendly objects.

Never return plain paragraphs.

Always return structured data.

Example

Recommendation

Confidence

Pros

Cons

Nearby

Summary

This keeps frontend independent of AI output format.

---

# AI Responsibilities

AI is responsible for

Natural language understanding

Reasoning

Property comparison

Recommendation explanation

Ranking

Generating summaries

AI is NOT responsible for

Conversation flow

State management

Memory

API routing

Business logic

Search triggering

Validation

Caching

---

# Free Tier Strategy

MoveMate AI is designed around free-tier limitations.

The backend should always attempt to avoid unnecessary LLM calls.

Examples

User changes budget

↓

Update memory

↓

Do not call Gemini immediately

Missing Area

↓

Ask directly

↓

No Gemini

Duplicate search

↓

Return cached response

↓

No Gemini

Only call the LLM when intelligence is required.

---

# Communication Flow

Every conversation follows the same pipeline.

User Message

↓

Conversation Manager

↓

Memory Update

↓

State Detection

↓

Decision Engine

↓

Need More Information?

↓

YES

↓

Generate Follow-up Question

OR

NO

↓

Tool Manager

↓

Tavily Search

↓

LLM Service

↓

Response Builder

↓

Frontend

---

# LLM Independence

The application should never depend directly on Gemini.

Conversation Manager should only call

LLMService.reason()

Internally

LLMService decides

Gemini

OpenAI

Claude

DeepSeek

Switching providers should require changes in only one module.

---

# Error Handling Philosophy

Users should never see technical failures.

Instead of

429

Timeout

Quota Exceeded

API Error

Shelby explains naturally.

Example

"I'm having a little trouble comparing listings right now.

Please try again in a few moments."

---

# Scalability

Version 1

Bangalore

↓

Version 2

Multiple Cities

↓

Version 3

User Accounts

↓

Version 4

Persistent Memory

↓

Version 5

Maps Integration

↓

Version 6

Voice

↓

Version 7

Image Search

The architecture should remain unchanged.

Only modules grow.

---

# Engineering Principles

Every module has one responsibility.

Every API returns structured data.

Every decision should be deterministic whenever possible.

LLMs should only reason.

Backend controls workflow.

Frontend controls presentation.

AI enhances decisions.

AI never controls the application.

---

# Summary

MoveMate AI is NOT an AI chatbot.

It is an AI-powered relocation platform.

The backend owns the conversation.

The LLM provides intelligence.

Shelby provides personality.

The user receives trusted recommendations.

---

End of Document