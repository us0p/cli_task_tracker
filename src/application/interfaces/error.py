from typing import TypedDict

UseCaseError = TypedDict(
    "UseCaseError",
    {"error": str},
    total=True
)
