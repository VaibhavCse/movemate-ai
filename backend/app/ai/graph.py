from langgraph.graph import START, StateGraph
from langgraph.prebuilt import ToolNode

from app.ai.memory import memory
from app.ai.nodes import chatbot_node
from app.ai.nodes.preferences import preference_node
from app.ai.routers import route_tools
from app.ai.state import ChatState
from app.ai.tools.registry import TOOLS


builder = StateGraph(ChatState)


# Preference extraction
builder.add_node(
    "preferences",
    preference_node,
)


# Main chatbot
builder.add_node(
    "chatbot",
    chatbot_node,
)


# Tool execution
builder.add_node(
    "tools",
    ToolNode(TOOLS),
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