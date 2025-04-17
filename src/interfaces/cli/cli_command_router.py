from tabulate import tabulate

from src.domain.repositories.task_repository import ITaskRepository
from src.controllers.task import TaskController


class CLICommandRouter:
    def __init__(self, repo: ITaskRepository):
        self.controller = TaskController(repo)

    def create_command(self, input_options):
        task = self.controller.create(
            {
                "status": input_options.status,
                "description": input_options.description,
            }
        )

        print(tabulate([task], headers="keys"))

    def read_command(self, input_options):
        tasks = self.controller.read(input_options.status)
        print(tabulate(tasks, headers="keys"))

    def update_command(self, input_options):
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
            return print(tabulate([task], headers="keys"))

        print(f"Task with ID '{input_options.id}' doesn't exist")

    def delete_command(self, input_options):
        task = self.controller.delete(input_options.id)

        if task:
            return print(tabulate([task], headers="keys"))

        print(f"Task with ID '{input_options.id}' doesn't exist")
