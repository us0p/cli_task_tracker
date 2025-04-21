from typing import List, Union

from src.application.mappers.task import TaskDict
from src.domain.repositories.task_repository import ITaskRepository
from src.controllers.task import TaskController


class CLICommandRouter:
    def __init__(self, repo: ITaskRepository):
        self.controller = TaskController(repo)

    def create_command(self, input_options) -> TaskDict:
        return self.controller.create(
            {
                "status": input_options.status,
                "description": input_options.description,
            }
        )

    def read_command(self, input_options) -> List[TaskDict]:
        return self.controller.read(input_options.status)

    def update_command(self, input_options) -> Union[TaskDict, str]:
        task = None
        if input_options.description:
            task = self.controller.update(
                input_options.id,
                {
                    "status": input_options.status,
                    "description": input_options.description,
                },
            )
        else:
            task = self.controller.update_status(
                input_options.id, input_options.status
            )

        if task:
            return task

        return f"Task with ID '{input_options.id}' doesn't exist"

    def delete_command(self, input_options) -> Union[TaskDict, str]:
        task = self.controller.delete(input_options.id)

        if task:
            return task

        return f"Task with ID '{input_options.id}' doesn't exist"
