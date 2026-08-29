from typing import Type

from pydantic import BaseModel, Field

from app.ai.tools.base import MoveMateTool


class RentEstimatorInput(BaseModel):
    locality: str = Field(description="Locality name.")
    bhk: int = Field(description="Number of bedrooms.")


class RentEstimatorTool(MoveMateTool):
    name: str = "rent_estimator"

    description: str = (
        "Estimate monthly rent for a locality."
    )

    args_schema: Type[BaseModel] = RentEstimatorInput

    def _run(
        self,
        locality: str,
        bhk: int,
    ):

        start = self.timed()

        mock_data = {
            "1": (18000, 25000),
            "2": (28000, 42000),
            "3": (40000, 65000),
        }

        low, high = mock_data.get(
            str(bhk),
            (25000, 45000),
        )

        return self.success_response(
            data={
                "locality": locality,
                "bhk": bhk,
                "estimated_rent_range": {
                    "min": low,
                    "max": high,
                },
            },
            message="Estimated rent generated.",
            # source="mock",
            execution_time_ms=(self.timed() - start) * 1000,
        )


rent_estimator_tool = RentEstimatorTool()