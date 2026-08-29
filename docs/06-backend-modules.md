# MoveMate AI - Backend Modules

Version: 1.0

Status: Approved

---

# Purpose

This document defines every backend module, its responsibilities, public methods, dependencies, and interactions.

Every module in MoveMate AI must follow the Single Responsibility Principle (SRP).

A module should do one thing and do it well.

---

# Backend Overview

The backend is divided into independent modules.

Each module communicates through well-defined interfaces.

```
Frontend
      │
      ▼
API Layer
      │
      ▼
Conversation Manager
      │
      ▼
Intent Detector
      │
      ▼
Change Detector
      │
      ▼
Decision Engine
      │
      ▼
Search Strategy Engine
      │
      ▼
Cache Manager
      │
      ▼
Tool Manager
      │
      ▼
LLM Service
      │
      ▼
Response Builder
```

---

# Conversation Manager

## Responsibility

Controls the entire conversation lifecycle.

Coordinates every other module.

Never performs AI reasoning.

---

## Public Methods

```python
start_session()

process_message()

update_memory()

get_next_action()

end_session()
```

---

## Depends On

- Memory Manager
- Intent Detector
- Change Detector
- Decision Engine

---

# Intent Detector

## Responsibility

Determines what the user wants.

Examples

New Search

Modify Search

Ask Question

Explain Recommendation

General Conversation

---

## Public Methods

```python
detect_intent()

classify_message()
```

---

## Output

```
NEW_SEARCH

UPDATE_SEARCH

EXPLAIN

FOLLOW_UP

GENERAL
```

---

# Change Detector

## Responsibility

Compares the latest user input with session memory.

Detects whether any meaningful information changed.

---

## Public Methods

```python
detect_changes()

has_search_changed()

has_preferences_changed()
```

---

## Example

Memory

Budget = 25000

User

"My budget is 30000"

↓

Budget Changed

↓

Return

```
SEARCH_REQUIRED
```

---

# Decision Engine

## Responsibility

Decides the next backend action.

Never communicates with AI directly.

---

## Public Methods

```python
decide()

should_search()

should_call_llm()

should_use_cache()
```

---

## Possible Outputs

```
ASK_CITY

ASK_BUDGET

ASK_AREA

SEARCH

USE_CACHE

RETURN_REPORT

ERROR
```

---

# Search Strategy Engine

## Responsibility

Plans how the search should be executed.

Examples

Area Expansion

Search Radius

Search Priority

Nearby Alternatives

---

## Public Methods

```python
build_search_plan()

expand_nearby_areas()

prioritize_locations()
```

---

## Example

Input

Office

Bellandur

Output

Bellandur

HSR Layout

Green Glen Layout

Sarjapur Road

---

# Cache Manager

## Responsibility

Stores and retrieves previous search results.

Reduces Tavily and LLM usage.

---

## Public Methods

```python
get()

set()

invalidate()

exists()
```

---

# Tool Manager

## Responsibility

Acts as a gateway to external services.

Never contains business logic.

---

## Version 1 Tools

Tavily

---

## Future

Google Maps

Travel Time APIs

Rental APIs

Maps

Weather

Vector Database

---

## Public Methods

```python
search()

invoke_tool()
```

---

# LLM Service

## Responsibility

Provides a unified interface for all language models.

The application never calls Gemini directly.

---

## Public Methods

```python
reason()

summarize()

rank()

explain()
```

---

## Providers

Gemini

Future

OpenAI

Claude

DeepSeek

---

# Response Builder

## Responsibility

Converts backend results into frontend-ready JSON.

Never performs reasoning.

---

## Public Methods

```python
build_question()

build_report()

build_error()
```

---

# Memory Manager

## Responsibility

Maintains conversation memory.

---

## Public Methods

```python
load()

save()

update()

clear()
```

---

# API Layer

## Responsibility

Expose REST endpoints.

Perform request validation.

Return HTTP responses.

No business logic.

---

# Module Dependencies

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

---

# Engineering Principles

Every module has one responsibility.

Every module should be independently testable.

Modules communicate through interfaces.

Business logic never exists inside API routes.

The LLM is a service, not the application.

---

End of Document