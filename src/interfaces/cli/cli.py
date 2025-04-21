from argparse import ArgumentParser, _SubParsersAction

from src.interfaces.cli.cli_command_router import CLICommandRouter


class CLI:
    def __init__(self, command_routes: CLICommandRouter):
        self._command_routes = command_routes
        self.parser = ArgumentParser(
            prog="Task Tracker", description="CLI Task manager"
        )

        subparser = self.parser.add_subparsers(
            dest="command", required=True
        )

        self._add_create_command(subparser)
        self._add_read_command(subparser)
        self._add_update_command(subparser)
        self._add_delete_command(subparser)

    def parse_cli(self):
        args = self.parser.parse_args()
        return args.func(args)

    def _add_create_command(self, subparser: _SubParsersAction):
        create_task_parser = subparser.add_parser(
            "create", help="Creates a new task"
        )
        create_task_parser.add_argument(
            "-s",
            "--status",
            required=True,
            choices=["todo", "in-progress", "done"],
            help="The status of the task",
        )
        create_task_parser.add_argument(
            "-d",
            "--description",
            required=True,
            help="A short description of the task",
        )
        create_task_parser.set_defaults(
            func=self._command_routes.create_command
        )

    def _add_read_command(self, subparser: _SubParsersAction):
        read_task_parser = subparser.add_parser(
            "read", help="Reads tasks in the store"
        )
        read_task_parser.add_argument(
            "-s",
            "--status",
            choices=["todo", "in-progress", "done"],
            help="List tasks with this status",
        )
        read_task_parser.set_defaults(
            func=self._command_routes.read_command
        )

    def _add_update_command(self, subparser: _SubParsersAction):
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
        update_task_parser.set_defaults(
            func=self._command_routes.update_command
        )

    def _add_delete_command(self, subparser: _SubParsersAction):
        delete_task_parser = subparser.add_parser(
            "delete", help="Deletes the provided command"
        )
        delete_task_parser.add_argument(
            "id", help="The ID of the task to delete"
        )
        delete_task_parser.set_defaults(
            func=self._command_routes.delete_command
        )
