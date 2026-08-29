# MoveMate AI - Data Model

Version: 1.0

Status: Approved

---

# Purpose

This document defines the core data models used throughout the application.

These models act as the contract between backend modules.

---

# Session

```python
Session
```

Fields

```
id

createdAt

updatedAt

currentState

memory

lastRecommendation
```

---

# User Memory

```python
UserMemory
```

Fields

```
city

budget

preferredArea

officeLocation

propertyType

preferences
```

---

# Preferences

```
parking

petFriendly

furnished

metroNearby

gymNearby

maxCommute

family

bachelor
```

---

# Conversation

```
Conversation
```

Fields

```
sessionId

messages

createdAt
```

---

# Message

```
Message
```

Fields

```
role

content

timestamp
```

Role

```
USER

SHELBY

SYSTEM
```

---

# Property

Fields

```
id

title

area

rent

matchScore

pros

cons

nearby

listingUrl
```

---

# Nearby

```
metro

gym

hospital

grocery
```

---

# Recommendation Report

```
summary

confidence

properties

nearbyAreas

nextSuggestion
```

---

# Search Plan

```
city

primaryArea

expandedAreas

budget

filters
```

---

# Search Result

```
properties

source

cached

searchTime
```

---

# Decision Result

```
action

reason

requiresSearch

requiresLLM

cacheHit
```

---

# Engineering Principles

Every model has one purpose.

Models should remain provider-independent.

Frontend and backend should share compatible schemas.

---

End of Document