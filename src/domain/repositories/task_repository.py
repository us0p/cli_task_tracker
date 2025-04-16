from abc import ABC, abstractmethod
from src.domain.entities.task.task import Task, TaskStatus


class ITaskRepository(ABC):
    @abstractmethod
    def create(self, task: Task) -> Task: ...

    @abstractmethod
    def update(self, task_id: str, new_task: Task) -> Task | None: ...

    @abstractmethod
    def delete(self, task_id: str) -> Task | None: ...

    @abstractmethod
    def update_status(
        self, task_id: str, status: TaskStatus
    ) -> Task | None: ...

    @abstractmethod
    def read_all(self) -> list[Task]: ...

    @abstractmethod
    def read_by_status(self, status: TaskStatus) -> list[Task]: ...
