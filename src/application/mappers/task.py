from datetime import datetime
from typing import TypedDict

from src.domain.entities.task.task import Task, TaskStatus

TaskDict = TypedDict(
    "TaskDict",
    {
        "id": str,
        "status": TaskStatus,
        "description": str,
        "createdAt": str,
        "updatedAt": str,
    },
    total=True,
)


class TaskDictMapper:
    @classmethod
    def task_to_dict(cls, task: Task) -> TaskDict:
        return {
            "id": task.id,
            "status": task.status,
            "description": task.description,
            "createdAt": task.createdAt.isoformat(),
            "updatedAt": task.updatedAt.isoformat(),
        }

    @classmethod
    def dict_to_task(cls, dictTask: TaskDict) -> Task:
        task = Task(
            dictTask["status"],
            dictTask["description"],
        )

        task.id = dictTask["id"]
        task.createdAt = datetime.fromisoformat(dictTask["createdAt"])
        task.updatedAt = datetime.fromisoformat(dictTask["updatedAt"])

        return task
