# MoveMate AI - Project Folder Structure

Version: 1.0

Status: Approved

---

# Purpose

Defines the recommended folder structure for MoveMate AI.

The structure is designed for scalability, maintainability, and clear separation of concerns.

---

# Repository Structure

```text
movemate-ai/

├── frontend/
│   ├── app/
│   ├── components/
│   ├── hooks/
│   ├── lib/
│   ├── services/
│   ├── types/
│   └── utils/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── conversation/
│   │   ├── decision/
│   │   ├── formatter/
│   │   ├── llm/
│   │   ├── memory/
│   │   ├── schemas/
│   │   ├── search/
│   │   ├── tools/
│   │   ├── core/
│   │   ├── utils/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── tests/
│   ├── requirements.txt
│   └── README.md
│
├── docs/
│
├── .gitignore
├── docker-compose.yml
├── README.md
└── LICENSE
```

---

# Backend Structure

```text
app/

api/
    chat.py

conversation/
    conversation_manager.py
    state_machine.py

decision/
    decision_engine.py
    intent_detector.py
    change_detector.py

memory/
    memory_manager.py

search/
    search_strategy.py
    cache_manager.py

tools/
    tool_manager.py
    tavily_client.py

llm/
    llm_service.py
    gemini_provider.py

formatter/
    response_builder.py

schemas/
    request.py
    response.py
    property.py
    report.py

core/
    config.py
    logging.py

utils/

main.py
```

---

# Frontend Structure

```text
app/
components/
hooks/
lib/
services/
types/
utils/
```

---

# Folder Responsibilities

| Folder | Responsibility |
|---------|----------------|
| api | REST endpoints |
| conversation | Conversation orchestration |
| decision | Business decisions |
| memory | Session memory |
| search | Search planning & cache |
| tools | External APIs |
| llm | AI providers |
| formatter | API response generation |
| schemas | Pydantic models |
| core | Configuration & logging |
| utils | Shared helpers |

---

# Principles

- One responsibility per folder.
- Business logic never belongs in API routes.
- AI providers are isolated.
- Easy to test.
- Easy to extend.
- Feature additions should require minimal restructuring.

---

End of Document