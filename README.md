# MoveMate AI

> Find your next home with AI, not endless scrolling.

MoveMate AI is an AI-powered relocation assistant that helps users explore rental properties and relocation-related information through natural conversations.

The system combines conversational AI, tool calling, web search, structured property extraction, and session-based conversation memory to provide relevant rental recommendations.

---

## Features

- Conversational rental property search
- AI-powered apartment recommendations
- Natural-language housing queries
- Budget and apartment-type based filtering
- Structured property information extraction
- Rental price estimation
- Locality and relocation tools
- Web search through Tavily
- Gemini-powered reasoning and summarization
- Session-based conversation memory
- Follow-up questions within the same session
- Modular tool-based architecture
- Basic application and provider error handling

---

## Example

A user can start with:

> I need a furnished 2 BHK in HSR under ₹30,000 with parking and no broker.

And then continue the same conversation:

> Actually increase my budget to ₹35,000.

MoveMate retains the conversation context within the session and can use the updated requirement when performing the next search.

---

## Architecture

```text
                         User
                           │
                           ▼
                    FastAPI Chat API
                           │
                           ▼
                     Chat Service
                           │
                           ▼
                       LangGraph
                           │
                  ┌────────┴────────┐
                  │                 │
                  ▼                 ▼
              Chatbot Node        Tools
                  │                 │
                  │        ┌────────┼────────┐
                  │        │        │        │
                  │     Housing   Search   Other
                  │      Tools     Tools   Tools
                  │        │
                  │        ▼
                  │   Apartment Service
                  │        │
                  │   ┌────┴─────┐
                  │   ▼          ▼
                  │ Tavily    Extraction
                  │ Search      Chain
                  │                │
                  │                ▼
                  │          Structured Listings
                  │
                  └──────────────┐
                                 ▼
                              Gemini
                                 │
                                 ▼
                              Response