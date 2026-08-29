from app.ai.tools.registry import TOOLS
from app.clients.llm import llm

llm_with_tools = llm.bind_tools(TOOLS)