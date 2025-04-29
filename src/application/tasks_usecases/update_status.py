from src.domain.entities.task.task import Task, TaskStatus
from src.domain.errors.validation import ValidationError
from src.domain.repositories.task_repository import ITaskRepository


class UpdateTaskStatusUseCase:
    @classmethod
    def exec(
        cls, repo: ITaskRepository, task_id: str, status: TaskStatus
    ) -> Task | None:
        if status not in ["done", "in-progress", "todo"]:
            raise ValidationError(f"'{status}' is not a valid TaskStatus")
        return repo.update_status(task_id, status)
