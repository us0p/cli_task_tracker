from src.domain.entities.task.task import TaskStatus, Task
from src.domain.repositories.task_repository import ITaskRepository


class ReadByStatusTaskUseCase:
    @classmethod
    def exec(cls, repo: ITaskRepository, status: TaskStatus) -> list[Task]:
        return repo.read_by_status(status)
