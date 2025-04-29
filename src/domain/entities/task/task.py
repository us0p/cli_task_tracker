from typing import Literal
from datetime import datetime, UTC
from uuid import uuid4

from src.domain.errors.validation import ValidationError

TaskStatus = Literal["todo", "in-progress", "done"]


class Task:
    def __init__(self, status: TaskStatus, description: str = ""):
        self.id = uuid4().hex
        self.status: TaskStatus = status
        self.description = description
        self.createdAt = datetime.now(UTC)
        self.updatedAt = datetime.now(UTC)

    def validate(self):
        if self.status not in ["todo", "in-progress", "done"]:
            raise ValidationError(f"'{self.status} is not a valid TaskStatus")
