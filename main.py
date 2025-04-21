from src.interfaces.cli.cli import CLI, CLICommandRouter
from src.interfaces.cli.cli_displayer import CLITabulator
from src.interfaces.repositories.task import TaskRepository

repo = TaskRepository()
command_routes = CLICommandRouter(repo)
cli = CLI(command_routes)

args = cli.parse_cli()

tabulator = CLITabulator(args)
print(tabulator.tabulate())
