# MoveMate AI - Decision Engine

Version: 1.0

Status: Approved

---

# Purpose

The Decision Engine is responsible for determining what Shelby should do after receiving every user message.

It acts as the central decision-making component of the backend.

Instead of immediately searching listings or calling an LLM, the Decision Engine evaluates the current conversation state, user intent, session memory, and available data before deciding the next action.

Its primary goal is to reduce unnecessary API calls while providing a fast and intelligent user experience.

---

# Responsibilities

The Decision Engine decides:

- Should Shelby ask another question?
- Is enough information available?
- Should cached results be used?
- Should a new search begin?
- Should the LLM be called?
- Should nearby areas be suggested?
- Should the conversation continue using previous recommendations?

The Decision Engine never generates responses.

It only decides the next action.

---

# Inputs

The Decision Engine receives

- Current User Message
- Session Memory
- Current Conversation State
- Previous Recommendations
- Search Cache Status

---

# Output

The Decision Engine returns a single action.

Examples

ASK_CITY

ASK_BUDGET

ASK_AREA

SEARCH

USE_CACHE

REASON

SHOW_REPORT

SUGGEST_NEARBY

HANDLE_ERROR

---

# Decision Flow

User Message

↓

Conversation Manager

↓

Memory Updated

↓

Decision Engine

↓

Determine Next Action

↓

Execute Action

---

# Decision Rules

The Decision Engine evaluates every message using a fixed sequence of checks.

---

## Rule 1

Is this a new conversation?

If yes

Initialize memory.

Ask for city.

---

## Rule 2

Is the city supported?

Supported

Bangalore

Unsupported

Return friendly message.

Remain in COLLECT_CITY.

---

## Rule 3

Is required information complete?

Required

- City
- Budget
- Area OR Office Location

If incomplete

Ask only the missing field.

---

## Rule 4

Has the user changed any information?

Examples

Budget changed

Area changed

Office changed

Property type changed

If nothing important changed

Do not perform another search.

---

## Rule 5

Can cached results be reused?

If matching cached results exist

Return cache.

Skip Tavily.

Skip Gemini.

---

## Rule 6

Is a fresh search required?

If user changes

Budget

Area

Office Location

Property Type

Perform a new search.

---

## Rule 7

Should the LLM be called?

Call the LLM only after

- Search completed
- Search results available
- Reasoning required

Never call the LLM for simple validation.

---

# Change Detection

The Decision Engine compares new input with session memory.

Example

Memory

Budget = ₹25k

User

"My budget is ₹25k"

No change detected.

No search required.

---

Memory

Budget = ₹25k

User

"My budget is ₹30k"

Budget changed.

Trigger new search.

---

Memory

Area = Bellandur

User

"Need parking."

Area unchanged.

Budget unchanged.

Search unchanged.

Only update preferences.

---

# Search Triggers

A fresh search should occur only when

- Budget changes
- Area changes
- Office location changes
- Property type changes
- User explicitly requests new options

Examples

"Show more options."

"Search nearby."

"Increase budget to ₹35k."

---

# Non-Search Actions

Some requests should never trigger a search.

Examples

"Why did you recommend this?"

"Explain the pros."

"Which metro is nearby?"

"Can you summarize?"

These should use existing recommendations whenever possible.

---

# Cache Strategy

Before every search

↓

Check cache

↓

If found

Return cached data

↓

Skip search

↓

Skip reasoning

If cache is invalid

Perform a new search.

---

# LLM Strategy

Never call the LLM for

- Greeting
- Validation
- Missing information
- Memory updates
- State transitions
- Cache checks

Only call the LLM for

- Ranking properties
- Comparing listings
- Explaining recommendations
- Generating summaries
- Confidence scoring

---

# Search Strategy

When searching

The Search Strategy Engine determines

- Which areas to search
- Nearby alternatives
- Search radius
- Search priority

Example

Office Location

Bellandur

↓

Search

Bellandur

HSR Layout

Green Glen Layout

Sarjapur Road

---

# Error Decisions

If Tavily fails

Retry once.

If retry fails

Return friendly error.

Do not crash the conversation.

---

If Gemini fails

Retry once.

If retry fails

Return available search results without AI explanation.

The conversation should continue.

---

# Performance Goals

The Decision Engine should

Minimize API calls.

Reuse cached data whenever possible.

Avoid unnecessary searches.

Keep average response time low.

Separate business logic from AI reasoning.

---

# Engineering Principles

The Decision Engine owns business decisions.

The Conversation Manager owns conversation flow.

The Search Strategy Engine owns search planning.

The Tool Manager owns external tools.

The LLM provides intelligence.

Every module has one responsibility.

---

# Summary

The Decision Engine is the traffic controller of MoveMate AI.

It decides what should happen next, minimizes unnecessary API usage, reuses existing information whenever possible, and ensures Shelby behaves efficiently and intelligently without relying on the LLM for application logic.

---

End of Document