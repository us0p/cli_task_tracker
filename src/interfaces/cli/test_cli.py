import pytest

from os import remove
from os.path import realpath, join, dirname

from src.interfaces.cli.cli import CLI
from src.interfaces.cli.cli_command_router import CLICommandRouter
from src.interfaces.repositories.task import TaskRepository


class TestCLI:
    @classmethod
    def setup_class(cls):
        repo = TaskRepository("test.db.json")
        command_router = CLICommandRouter(repo)
        cls._cli = CLI(command_router)


    @classmethod
    def teardown_class(cls):
        remove(realpath(join(
            dirname(__file__), "..", "..", "..", "test.db.json"
        )))
        

    def test_create_requires_status(self, capsys):
        with pytest.raises(SystemExit):
            type(self)._cli.parser.parse_args(["create"])

        captured = capsys.readouterr()

        assert (
            "error: the following arguments are required: -s/--status"
            in captured.err
        )

    def test_create_status_with_wrong_option(self, capsys):
        with pytest.raises(SystemExit):
            type(self)._cli.parser.parse_args(["create", "-s", "test"])

        captured = capsys.readouterr()

        assert (
            "error: argument -s/--status: invalid choice: 'test'" in captured.err
        )

    def test_create_requires_description(self, capsys):
        with pytest.raises(SystemExit):
            type(self)._cli.parser.parse_args(["create", "-s", "todo"])

        captured = capsys.readouterr()

        assert (
            "error: the following arguments are required: -d/--description"
            in captured.err
        )

    def test_update_require_id(self, capsys):
        with pytest.raises(SystemExit):
            type(self)._cli.parser.parse_args(["update"])

        captured = capsys.readouterr()

        assert (
            "error: the following arguments are required: id, -s/--status"
            in captured.err
        )

    def test_update_requires_status(self, capsys):
        with pytest.raises(SystemExit):
            type(self)._cli.parser.parse_args(["update", "1234asdf"])

        captured = capsys.readouterr()

        assert (
            "error: the following arguments are required: -s/--status"
            in captured.err
        )

    def test_update_status_with_wrong_option(self, capsys):
        with pytest.raises(SystemExit):
            type(self)._cli.parser.parse_args(["update", "-s", "test"])

        captured = capsys.readouterr()

        assert (
            "error: argument -s/--status: invalid choice: 'test'" in captured.err
        )

    def test_delete_require_id(self, capsys):
        with pytest.raises(SystemExit):
            type(self)._cli.parser.parse_args(["delete"])

        captured = capsys.readouterr()

        assert "error: the following arguments are required: id" in captured.err
