from json import dumps, loads
from datetime import datetime, UTC

from src.domain.entities.task.task import Task
from src.domain.repositories.task_repository import ITaskRepository

from src.application.mappers.task import (
    TaskDict,
    TaskDictMapper,
    TaskStatus,
)
from src.interfaces.drivers.file_access import JsonDB


class TaskRepository(ITaskRepository, JsonDB):
    def _read_all_dict(self) -> list[TaskDict]:
        with open(self._file_name, "r") as f:
            return loads(f.read())

    def create(self, task: Task) -> Task:
        tasks = self._read_all_dict()
        tasks.append(TaskDictMapper.task_to_dict(task))
        with open(self._file_name, "w") as f:
            tasks_json = dumps(tasks)
            f.write(tasks_json)

        return task

    def update(self, task_id: str, new_task: Task) -> Task | None:
        tasks = self._read_all_dict()
        updated_task = None
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = new_task.status
                task["description"] = new_task.description
                task["updatedAt"] = datetime.now(UTC).isoformat()
                updated_task = TaskDictMapper.dict_to_task(task)
                break

        with open(self._file_name, "w") as f:
            f.write(dumps(tasks))

        return updated_task

    def delete(self, task_id: str) -> Task | None:
        tasks = self._read_all_dict()
        updated_tasks = []
        deleted_task = None

        for task in tasks:
            if task["id"] == task_id:
                deleted_task = TaskDictMapper.dict_to_task(task)
                continue
            updated_tasks.append(task)

        with open(self._file_name, "w") as f:
            f.write(dumps(updated_tasks))

        return deleted_task

    def read_all(self) -> list[Task]:
        tasks_as_dict = self._read_all_dict()
        return [
            TaskDictMapper.dict_to_task(task) for task in tasks_as_dict
        ]

    def read_by_status(self, status: TaskStatus) -> list[Task]:
        tasks = self.read_all()

        return [task for task in tasks if task.status == status]
