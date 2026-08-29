from app.ai.tools.finance.calculator import calculator_tool
from app.ai.tools.housing.apartment_search import apartment_search_tool
from app.ai.tools.housing.rent_estimator import rent_estimator_tool

TOOLS = [
    calculator_tool,
    apartment_search_tool,
    rent_estimator_tool,
]