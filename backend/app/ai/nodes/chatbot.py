from app.ai.models import llm_with_tools
from app.ai.prompts import SYSTEM_MESSAGE
from app.ai.state import ChatState


async def chatbot_node(state: ChatState):

    conversation_messages = state.get("messages", [])

    if not conversation_messages:
        raise ValueError(
            "Chatbot received no conversation messages."
        )

    messages = [
        SYSTEM_MESSAGE,
        *conversation_messages,
    ]

    response = await llm_with_tools.ainvoke(messages)

    return {
        "messages": [response],
    }