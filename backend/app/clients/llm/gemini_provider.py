from typing import TypeVar

from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel

from app.core.config import settings
from app.core.exceptions import AIProviderError


llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=settings.GOOGLE_API_KEY,
    temperature=0.3,
    max_retries=1,
)


T = TypeVar("T", bound=BaseModel)


class GeminiProvider:
    async def generate(self, prompt: str) -> str:
        try:
            response = await llm.ainvoke(
                [HumanMessage(content=prompt)]
            )
            return self._extract_text(response.content)

        except Exception as exc:
            raise self._handle_error(exc) from exc

    async def generate_structured(
        self,
        prompt: str,
        schema: type[T],
    ) -> T:
        try:
            structured_llm = llm.with_structured_output(schema)

            return await structured_llm.ainvoke(
                [HumanMessage(content=prompt)]
            )

        except Exception as exc:
            raise self._handle_error(exc) from exc

    @staticmethod
    def _handle_error(exc: Exception) -> AIProviderError:
        error_text = str(exc).lower()

        if (
            "resourceexhausted" in error_text
            or "quota exceeded" in error_text
            or "quota" in error_text
            or "rate limit" in error_text
            or "429" in error_text
        ):
            return AIProviderError(
                message=str(exc),
                user_message=(
                    "Shelby is temporarily unavailable because "
                    "the AI usage limit has been reached. "
                    "Please try again later."
                ),
            )

        return AIProviderError(
            message=str(exc),
            user_message=(
                "Shelby is temporarily unavailable right now. "
                "Please try again in a moment."
            ),
        )

    @staticmethod
    def _extract_text(content) -> str:
        if isinstance(content, str):
            return content.strip()

        if isinstance(content, list):
            texts = []

            for block in content:
                if isinstance(block, dict):
                    if block.get("type") == "text":
                        texts.append(block.get("text", ""))

                elif hasattr(block, "text"):
                    texts.append(block.text)

                else:
                    texts.append(str(block))

            return "\n".join(texts).strip()

        return str(content).strip()