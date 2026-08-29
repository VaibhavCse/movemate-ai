from app.ai.models import llm
from app.ai.prompts import chat_prompt


chat_chain = chat_prompt | llm