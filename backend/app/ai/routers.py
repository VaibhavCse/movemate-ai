from langgraph.graph import END

from app.ai.state import ChatState


def route_tools(state: ChatState):
    """
    Decide whether the chatbot wants to call a tool.
    """

    last_message = state["messages"][-1]

    if getattr(last_message, "tool_calls", None):
        return "tools"

    return END