from src.domain.entities.task.task import Task, TaskStatus
from src.domain.repositories.task_repository import ITaskRepository


class UpdateTaskStatusUseCase:
    @classmethod
    def exec(
        cls, repo: ITaskRepository, task_id: str, status: TaskStatus
    ) -> Task | None:
        return repo.update_status(task_id, status)
