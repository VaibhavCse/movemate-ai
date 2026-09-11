from langgraph.graph import START, StateGraph
from langgraph.prebuilt import ToolNode
from langgraph.types import RetryPolicy

from app.ai.memory import memory
from app.ai.nodes import chatbot_node
from app.ai.nodes.preferences import preference_node
from app.ai.routers import route_tools
from app.ai.state import ChatState
from app.ai.tools.registry import TOOLS
from app.core.exceptions import AIProviderError


def retry_without_ai_provider_error(exc: Exception) -> bool:
    """
    Retry transient errors, but never retry AI provider failures.

    AIProviderError already represents a normalized Gemini/provider
    failure, so retrying it at the LangGraph level only adds latency
    and can multiply API usage.
    """
    return not isinstance(exc, AIProviderError)


retry_policy = RetryPolicy(
    retry_on=retry_without_ai_provider_error,
)


builder = StateGraph(ChatState)


# Preference extraction
builder.add_node(
    "preferences",
    preference_node,
    retry_policy=retry_policy,
)


# Main chatbot
builder.add_node(
    "chatbot",
    chatbot_node,
    retry_policy=retry_policy,
)


# Tool execution
builder.add_node(
    "tools",
    ToolNode(TOOLS),
    retry_policy=retry_policy,
)


# START → preferences → chatbot
builder.add_edge(
    START,
    "preferences",
)

builder.add_edge(
    "preferences",
    "chatbot",
)


# Chatbot → tools or END
builder.add_conditional_edges(
    "chatbot",
    route_tools,
)


# Tools → chatbot
builder.add_edge(
    "tools",
    "chatbot",
)


graph = builder.compile(
    checkpointer=memory,
)