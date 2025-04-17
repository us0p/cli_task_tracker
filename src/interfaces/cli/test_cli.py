import pytest
from sys import stderr

from src.interfaces.cli.cli import CLI
from src.interfaces.cli.cli_command_router import CLICommandRouter
from src.interfaces.repositories.task import TaskRepository


class TestCLI:
    @pytest.fixture(autouse=True)
    def _configure_cli(self):
        repo = TaskRepository("test.db.json")
        command_router = CLICommandRouter(repo)
        self._cli = CLI(command_router)

    @pytest.fixture(autouse=True)
    def _patch_stderr_write(self):
        original_writer = stderr.write
        self.output = []

        def _stderr_write(
            message: str,
        ) -> int:
            self.output.append(message)
            return original_writer(message)

        stderr.write = _stderr_write
        yield
        stderr.write = original_writer

    def test_create_requires_status(self):
        with pytest.raises(SystemExit):
            self._cli.parser.parse_args(["create"])

        _, error = self.output

        assert (
            "error: the following arguments are required: -s/--status"
            in error
        )

    def test_create_status_with_wrong_option(self):
        with pytest.raises(SystemExit):
            self._cli.parser.parse_args(["create", "-s", "test"])

        _, error = self.output

        assert (
            "error: argument -s/--status: invalid choice: 'test'" in error
        )

    def test_create_requires_description(self):
        with pytest.raises(SystemExit):
            self._cli.parser.parse_args(["create", "-s", "todo"])

        _, error = self.output

        assert (
            "error: the following arguments are required: -d/--description"
            in error
        )

    def test_update_require_id(self):
        with pytest.raises(SystemExit):
            self._cli.parser.parse_args(["update"])

        _, error = self.output

        assert (
            "error: the following arguments are required: id, -s/--status"
            in error
        )

    def test_update_requires_status(self):
        with pytest.raises(SystemExit):
            self._cli.parser.parse_args(["update", "1234asdf"])

        _, error = self.output

        assert (
            "error: the following arguments are required: -s/--status"
            in error
        )

    def test_update_status_with_wrong_option(self):
        with pytest.raises(SystemExit):
            self._cli.parser.parse_args(["update", "-s", "test"])

        _, error = self.output

        assert (
            "error: argument -s/--status: invalid choice: 'test'" in error
        )

    def test_delete_require_id(self):
        with pytest.raises(SystemExit):
            self._cli.parser.parse_args(["delete"])

        _, error = self.output

        assert "error: the following arguments are required: id" in error
