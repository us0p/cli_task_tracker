from src.domain.repositories.task_repository import ITaskRepository
from src.domain.entities.task.task import Task


class ReadAllTaskUseCase:
    @classmethod
    def exec(cls, repo: ITaskRepository) -> list[Task]:
        return repo.read_all()
