from src.interfaces.cli.cli import CLI, CLICommandRouter
from src.interfaces.repositories.task import TaskRepository

repo = TaskRepository()
command_routes = CLICommandRouter(repo)
cli = CLI(command_routes)

# Should return args and share it with an ConsoleDipslay class
# That class should parse task data to be more compatible with console display
# Should test that class to ensure only relevant data is beeing displayed.
cli.parse_cli()
