from src.application.interfaces.task_input import TaskInputs
from src.domain.entities.task.task import Task
from src.domain.repositories.task_repository import ITaskRepository


class CreateTaskUseCase:
    @classmethod
    def exec(cls, repo: ITaskRepository, task_input: TaskInputs) -> Task:
        task = Task(task_input["status"], task_input["description"])
        return repo.create(task)
