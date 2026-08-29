# MoveMate AI - Conversation State Machine

Version: 1.0

Status: Approved

---

# Purpose

This document defines how Shelby manages every conversation.

Instead of responding directly to every user message, Shelby moves through a series of predefined conversation states.

This makes conversations:

- Predictable
- Easy to debug
- Easy to test
- Easy to extend
- Independent of the LLM

The Conversation Manager is responsible for controlling these states.

---

# Why a State Machine?

Traditional chatbots simply receive a message and generate a response.

MoveMate AI works differently.

Every message changes the current conversation state.

Example

User

"I need a flat."

↓

State

Collect City

↓

User

"Bangalore"

↓

State

Collect Budget

↓

User

"25k"

↓

State

Collect Area

↓

User

"Bellandur"

↓

State

Search

↓

Recommendation

This makes Shelby behave like a real relocation consultant.

---

# State Flow

START

↓

COLLECT_CITY

↓

COLLECT_BUDGET

↓

COLLECT_AREA

↓

READY_TO_SEARCH

↓

SEARCHING

↓

REASONING

↓

BUILDING_REPORT

↓

RECOMMENDATION_READY

↓

WAITING_FOR_NEXT_REQUEST

---

# Conversation States

---

## START

Purpose

Beginning of a new conversation.

Required Action

Initialize session memory.

Next State

COLLECT_CITY

---

## COLLECT_CITY

Purpose

Determine the city.

Validation

Only Bangalore is supported.

If another city is provided

Remain in this state.

Response

"I'm currently helping users relocate within Bangalore. Support for additional cities will be available in future versions."

Next State

COLLECT_BUDGET

---

## COLLECT_BUDGET

Purpose

Collect user's monthly budget.

Examples

15k

25000

₹30,000

Validation

Budget must be numeric.

Reasonable range

₹5,000 – ₹2,00,000

If invalid

Remain in this state.

Next State

COLLECT_AREA

---

## COLLECT_AREA

Purpose

Collect either

Preferred Area

OR

Office Location

Examples

HSR Layout

Bellandur

Whitefield

Koramangala

Electronic City

Validation

Accept either

Area

Office Location

Next State

READY_TO_SEARCH

---

## READY_TO_SEARCH

Purpose

Verify all required information exists.

Required

✓ City

✓ Budget

✓ Area OR Office Location

If any information is missing

Return to the required collection state.

Otherwise

SEARCHING

---

## SEARCHING

Purpose

Collect listing information.

Responsibilities

Call Search Strategy Engine.

↓

Call Tool Manager.

↓

Call Tavily.

No LLM reasoning happens here.

Next State

REASONING

---

## REASONING

Purpose

Analyze search results.

Responsibilities

Compare listings.

Rank properties.

Generate recommendations.

Suggest nearby areas.

Generate confidence score.

Gemini is used only in this state.

Next State

BUILDING_REPORT

---

## BUILDING_REPORT

Purpose

Convert AI output into structured objects.

Responsibilities

Property Objects

Recommendation Report

Summary

Confidence

Nearby Areas

Pros

Cons

No AI calls.

Next State

RECOMMENDATION_READY

---

## RECOMMENDATION_READY

Purpose

Return response to frontend.

Next State

WAITING_FOR_NEXT_REQUEST

---

## WAITING_FOR_NEXT_REQUEST

Purpose

Conversation remains active.

Shelby remembers previous context.

Examples

User

Need parking.

User

Increase budget to 30k.

User

Show more options.

User

Any metro nearby?

These requests do not restart the conversation.

The Conversation Manager updates memory and determines the next action.

---

# State Transitions

START

↓

COLLECT_CITY

↓

COLLECT_BUDGET

↓

COLLECT_AREA

↓

READY_TO_SEARCH

↓

SEARCHING

↓

REASONING

↓

BUILDING_REPORT

↓

RECOMMENDATION_READY

↓

WAITING_FOR_NEXT_REQUEST

---

# State Validation Rules

Every state must validate its own input.

Example

COLLECT_BUDGET

Accept

₹25k

25000

25 thousand

Reject

Cheap

Affordable

Lowest possible

---

# Search Conditions

Search should begin only when:

City exists

Budget exists

Area OR Office Location exists

Otherwise

Continue collecting information.

---

# Memory Rules

Conversation memory stores

City

Budget

Area

Office Location

Preferences

Latest Recommendation

Conversation History

The state machine always uses memory before asking another question.

Shelby must never ask the same question twice during one session.

---

# Search Strategy

If Area is unavailable but Office Location exists

↓

Generate nearby recommended areas

↓

Search those areas

Example

Office

Bellandur

↓

Search

HSR Layout

Green Glen Layout

Sarjapur Road

Bellandur

This logic belongs to the Search Strategy Engine.

---

# Poor Results

If search quality is low

Do NOT end the conversation.

Instead

Suggest nearby locations.

Example

"I couldn't find strong matches in HSR Layout under ₹18k.

Would you like me to search BTM Layout, Koramangala or Sarjapur Road?"

Conversation remains active.

---

# Unsupported City

If user requests

Jaipur

Mumbai

Delhi

Hyderabad

Response

"I'm currently helping users relocate within Bangalore.

Support for additional cities will be available in future versions."

Remain in

COLLECT_CITY

---

# Error Handling

Technical failures should never change the conversation state.

Example

Gemini Timeout

↓

Remain in

REASONING

↓

Retry

or

Return friendly message.

The conversation should continue normally.

---

# Future States

Version 2

VOICE_INPUT

IMAGE_ANALYSIS

ACCOUNT_LOGIN

MAP_VIEW

FAVORITES

PROPERTY_COMPARISON

SAVED_SEARCH

These can be added without changing existing states.

---

# State Machine Principles

Every conversation starts at START.

Every state has one responsibility.

Every transition is deterministic.

The Conversation Manager owns all state transitions.

Gemini never decides conversation flow.

The backend controls the conversation.

The LLM provides intelligence.

---

# Summary

The Conversation State Machine is the backbone of MoveMate AI.

It ensures Shelby asks the right questions, remembers context, performs searches only when enough information is available, and always returns structured recommendations while maintaining a natural conversation.

---

End of Document