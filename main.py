from src.interfaces.cli.cli import CLI
from src.interfaces.repositories.task import TaskRepository

repo = TaskRepository()
cli = CLI(repo)

cli.parse_cli()
