from argparse import ArgumentParser
from tabulate import tabulate

from src.interfaces.repositories.task import TaskRepository
from src.controllers.task import TaskController


class CLI:
    def __init__(self):
        self.repo = TaskRepository()
        self.controller = TaskController(self.repo)
        self.parser = ArgumentParser(
            prog="Task Tracker", description="CLI Task manager"
        )

        subparser = self.parser.add_subparsers()

        # Create command
        create_task_parser = subparser.add_parser(
            "create", help="Creates a new task"
        )
        create_task_parser.add_argument(
            "-s",
            "--status",
            type=str,
            required=True,
            choices=["todo", "in-progress", "done"],
            help="The status of the task",
        )
        create_task_parser.add_argument(
            "-d",
            "--description",
            type=str,
            required=True,
            help="A short description of the task",
        )
        create_task_parser.set_defaults(func=self.create_task)

        # Read command
        read_task_parser = subparser.add_parser(
            "read", help="Reads tasks in the store"
        )
        read_task_parser.add_argument(
            "-s",
            "--status",
            choices=["todo", "in-progress", "done"],
            help="List tasks with this status",
        )
        read_task_parser.set_defaults(func=self.read_tasks)

        # Update command
        update_task_parser = subparser.add_parser(
            "update", help="Updates the task as a whole"
        )
        update_task_parser.add_argument(
            "id", help="The ID of the task to update"
        )
        update_task_parser.add_argument(
            "-s",
            "--status",
            required=True,
            choices=["todo", "in-progress", "done"],
            help="The status of the task",
        )
        update_task_parser.add_argument(
            "-d",
            "--description",
            help="A short description of the task",
        )
        update_task_parser.set_defaults(func=self.update_task)

        # Delete command
        delete_task_parser = subparser.add_parser(
            "delete", help="Deletes the provided command"
        )
        delete_task_parser.add_argument(
            "id", help="The ID of the task to delete"
        )
        delete_task_parser.set_defaults(func=self.delete_task)

    def parse_cli(self):
        args = self.parser.parse_args()

        try:
            args.func(args)
        except AttributeError:
            self.parser.print_help()

    def create_task(self, input_options):
        task = self.controller.create(
            {
                "status": input_options.status,
                "description": input_options.description,
            }
        )

        print(tabulate([task], headers="keys"))

    def read_tasks(self, input_options):
        tasks = self.controller.read(input_options.status)
        print(tabulate(tasks, headers="keys"))

    def delete_task(self, input_options):
        task = self.controller.delete(input_options.id)

        if task:
            return print(tabulate([task], headers="keys"))

        print(f"Task with ID '{input_options.id}' doesn't exist")

    def update_task(self, input_options):
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
