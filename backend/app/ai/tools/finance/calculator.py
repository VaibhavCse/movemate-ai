from typing import Type

from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field

from app.ai.tools.base import MoveMateTool


class CalculatorInput(BaseModel):
    expression: str = Field(
        description="Mathematical expression to evaluate."
    )


class CalculatorTool(MoveMateTool):
    name: str = "calculator"
    description: str = (
        "Evaluate mathematical expressions."
    )

    args_schema: Type[BaseModel] = CalculatorInput

    def _run(self, expression: str):

        start = self.timed()

        try:
            result = eval(expression)

            return self.success_response(
                data={
                    "expression": expression,
                    "result": result,
                },
                message="Calculation completed successfully.",
                execution_time_ms=(self.timed() - start) * 1000,
            )

        except Exception as e:
            return self.error_response(
                message=str(e),
                execution_time_ms=(self.timed() - start) * 1000,
            )


calculator_tool = CalculatorTool()