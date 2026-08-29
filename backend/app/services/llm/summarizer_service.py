from app.clients.llm import GeminiProvider


class SummarizerService:

    def __init__(
        self,
        provider: GeminiProvider,
    ):
        self.provider = provider

    async def summarize(
        self,
        title: str,
        content: str,
    ) -> str:

        prompt = f"""
You are MoveMate AI.

Task:
Summarize the following information into a clean, user-friendly response.

Guidelines:
- Keep the response concise.
- Preserve important facts.
- Remove duplicate information.
- Use bullet points where appropriate.
- Do not make up information.
- If information is missing, say so.

Context:
{title}

Content:
{content}
"""

        return await self.provider.generate(prompt)