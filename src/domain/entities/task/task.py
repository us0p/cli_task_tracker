from typing import Literal
from datetime import datetime, UTC
from uuid import uuid4

TaskStatus = Literal["todo", "in-progress", "done"]


class Task:
    def __init__(self, status: TaskStatus, description: str = ""):
        self.id = uuid4()
        self.status = status
        self.description = description
        self.createdAt = datetime.now(UTC)
        self.updatedAt = datetime.now(UTC)
