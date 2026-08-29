from uuid import uuid4

from langchain_core.messages import HumanMessage

from app.ai.graph import graph
from app.schemas import ChatRequest, ChatResponse


class ChatService:

    async def process_message(
        self,
        request: ChatRequest,
    ) -> ChatResponse:

        session_id = request.session_id or str(uuid4())

        result = await graph.ainvoke(
            {
                "messages": [
                    HumanMessage(content=request.message)
                ],
                "session_id": session_id,
            },
            config={
                "configurable": {
                    "thread_id": session_id,
                }
            },
        )

        last_message = result["messages"][-1]

        return ChatResponse(
            reply=str(last_message.content),
            session_id=session_id,
        )


chat_service = ChatService()