from typing import TypeVar

from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel

from app.core.config import settings


llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=settings.GOOGLE_API_KEY,
    temperature=0.3,
)

T = TypeVar("T", bound=BaseModel)


class GeminiProvider:
    """
    Provider responsible for interacting with the configured Gemini model.
    """

    async def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generate plain text from Gemini.
        """

        response = await llm.ainvoke(
            [HumanMessage(content=prompt)]
        )

        return self._extract_text(response.content)

    async def generate_structured(
        self,
        prompt: str,
        schema: type[T],
    ) -> T:
        """
        Generate structured output using a Pydantic schema.
        This will be used later for property extraction,
        itinerary generation, relocation plans, etc.
        """

        structured_llm = llm.with_structured_output(schema)

        return await structured_llm.ainvoke(
            [HumanMessage(content=prompt)]
        )

    @staticmethod
    def _extract_text(content) -> str:
        """
        Safely extract plain text from LangChain response content.
        Supports both string and block-based responses.
        """

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