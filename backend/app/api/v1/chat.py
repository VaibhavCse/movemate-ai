"""
Chat API endpoints.
"""

import logging

from fastapi import APIRouter, HTTPException

from app.core.exceptions import MoveMateError
from app.schemas import ChatRequest, ChatResponse
from app.services.chat_service import chat_service

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post(
    "",
    response_model=ChatResponse,
    summary="Chat with Shelby",
    description="Accepts a user message and returns Shelby's response.",
)
async def chat(request: ChatRequest) -> ChatResponse:
    """
    Chat endpoint.

    Args:
        request: Incoming chat request.

    Returns:
        Chat response.
    """

    try:
        return await chat_service.process_message(request)

    except MoveMateError as exc:
        logger.warning(
            "MoveMate error during chat: %s",
            exc,
        )

        raise HTTPException(
            status_code=503,
            detail=exc.user_message,
        ) from exc

    except Exception as exc:
        logger.exception(
            "Unexpected error during chat request."
        )

        raise HTTPException(
            status_code=500,
            detail=(
                "I'm sorry, something went wrong while processing "
                "your request. Please try again."
            ),
        ) from exc