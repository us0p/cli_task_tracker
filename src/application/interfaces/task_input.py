from typing import TypedDict
from src.domain.entities.task.task import TaskStatus

TaskInputs = TypedDict(
    "TaskInputs",
    {"status": TaskStatus, "description": str},
    total=True,
)
