from app.ai.prompts.apartment_extraction import APARTMENT_EXTRACTION_PROMPT
from app.clients.llm.gemini_provider import GeminiProvider
from app.schemas.apartment import ApartmentExtractionResponse


class ApartmentExtractionChain:
    """
    AI chain responsible for extracting structured apartment
    information from raw search results.
    """

    def __init__(
        self,
        provider: GeminiProvider,
    ):
        self.provider = provider

    async def invoke(
        self,
        content: str,
    ) -> ApartmentExtractionResponse:
        """
        Extract structured apartment listings from raw search content.
        """

        prompt = APARTMENT_EXTRACTION_PROMPT.format(
            content=content,
        )

        return await self.provider.generate_structured(
            prompt=prompt,
            schema=ApartmentExtractionResponse,
        )