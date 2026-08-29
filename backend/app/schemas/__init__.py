"""
Pydantic schemas used throughout the MoveMate AI backend.
"""

from .request import ChatRequest
from .response import ChatResponse

__all__ = [
    "ChatRequest",
    "ChatResponse",
]