from typing import Annotated, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

from app.schemas.preferences import UserPreferences


class ChatState(TypedDict):
    messages: Annotated[
        list[BaseMessage],
        add_messages,
    ]

    session_id: str

    preferences: UserPreferences | None