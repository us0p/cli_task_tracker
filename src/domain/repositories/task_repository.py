from abc import ABC, abstractmethod
from src.domain.entities.task.task import Task, TaskStatus


class TaskRepository(ABC):
    @abstractmethod
    def create(self, task: Task) -> Task: ...

    @abstractmethod
    def update(self, task_id: str, new_task: Task) -> Task: ...

    @abstractmethod
    def delete(self, task_id: str) -> Task: ...

    @abstractmethod
    def update_status(self, task_id: str, status: TaskStatus) -> Task: ...

    @abstractmethod
    def read_all(self) -> list[Task]: ...

    @abstractmethod
    def read_by_status(self, status: TaskStatus) -> list[Task]: ...
