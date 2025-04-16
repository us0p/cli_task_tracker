from src.domain.repositories.task_repository import ITaskRepository
from src.domain.entities.task.task import Task


class DeleteTaskUseCase:
    @classmethod
    def exec(cls, repo: ITaskRepository, task_id: str) -> Task | None:
        return repo.delete(task_id)
