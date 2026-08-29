from time import perf_counter
from typing import Any

from langchain_core.tools import BaseTool


class MoveMateTool(BaseTool):
    """
    Base class for all MoveMate AI tools.
    """

    def timed(self) -> float:
        return perf_counter()

    def success_response(
        self,
        *,
        data: Any,
        message: str = "Success",
        execution_time_ms: float | None = None,
    ) -> dict:
        return {
            "success": True,
            "message": message,
            "execution_time_ms": execution_time_ms,
            "data": data,
        }

    def error_response(
        self,
        *,
        message: str,
        execution_time_ms: float | None = None,
    ) -> dict:
        return {
            "success": False,
            "message": message,
            "execution_time_ms": execution_time_ms,
            "data": None,
        }