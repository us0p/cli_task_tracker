from src.application.interfaces.task_input import TaskInputs
from src.domain.entities.task.task import Task
from src.domain.repositories.task_repository import ITaskRepository


class UpdateTaskUseCase:
    @classmethod
    def exec(
        cls,
        repo: ITaskRepository,
        task_id: str,
        new_task: TaskInputs,
    ) -> Task | None:
        task = Task(new_task["status"], new_task["description"])
        task.id = task_id
        return repo.update(task_id, task)
