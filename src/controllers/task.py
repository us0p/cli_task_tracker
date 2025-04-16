from typing import Optional
from src.application.interfaces.task_input import TaskInputs
from src.application.mappers.task import TaskDict, TaskDictMapper
from src.application.tasks_usecases.create import CreateTaskUseCase
from src.application.tasks_usecases.delete import DeleteTaskUseCase
from src.application.tasks_usecases.read_all import ReadAllTaskUseCase
from src.application.tasks_usecases.update import UpdateTaskUseCase
from src.application.tasks_usecases.read_by_status import (
    ReadByStatusTaskUseCase,
)
from src.domain.entities.task.task import Task, TaskStatus
from src.domain.repositories.task_repository import ITaskRepository


class TaskController:
    def __init__(self, repo: ITaskRepository):
        self.repo = repo

    def create(self, task_inputs: TaskInputs) -> TaskDict:
        task = CreateTaskUseCase.exec(self.repo, task_inputs)

        return TaskDictMapper.task_to_dict(task)

    def read(self, task_status: Optional[TaskStatus]) -> list[TaskDict]:
        tasks: list[Task] = []

        if task_status:
            tasks = ReadByStatusTaskUseCase.exec(self.repo, task_status)
        else:
            tasks = ReadAllTaskUseCase.exec(self.repo)

        return [TaskDictMapper.task_to_dict(task) for task in tasks]

    def update(
        self, task_id: str, task_inputs: TaskInputs
    ) -> TaskDict | None:
        task = UpdateTaskUseCase.exec(self.repo, task_id, task_inputs)

        if not task:
            return None

        return TaskDictMapper.task_to_dict(task)

    def delete(self, task_id: str) -> TaskDict | None:
        task = DeleteTaskUseCase.exec(self.repo, task_id)

        if not task:
            return None

        return TaskDictMapper.task_to_dict(task)
