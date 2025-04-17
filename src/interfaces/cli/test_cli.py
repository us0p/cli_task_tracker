import pytest
from sys import stderr

from src.interfaces.cli.cli import CLI
from src.interfaces.repositories.task import TaskRepository


class TestCLI:
    @pytest.fixture(autouse=True)
    def _configure_cli(self):
        repo = TaskRepository("test.db.json")
        self._cli = CLI(repo)

    @pytest.fixture(autouse=True)
    def _patch_stderr_write(self):
        oritinal_writer = stderr.write
        self.output = []

        def _stderr_write(
            message: str,
        ) -> int:
            self.output.append(message)
            return oritinal_writer(message)

        stderr.write = _stderr_write
        yield
        stderr.write = oritinal_writer

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

    def test_create_return_only_meaningful_data(self):
        # Get the response from the controller without tabulation
        args = self._cli.parser.parse_args(
            ["create", "-s", "todo", "-d", "Finish tests"]
        )
        args.func(args)
        print(args)
        assert 0

    def test_update_requires_status(self):
        pass

    def test_update_status_with_wrong_option(self):
        pass

    def test_update_return_only_meaningful_data(self):
        pass

    def test_read_return_only_meaningful_data(self):
        pass

    def test_delete_return_only_meaningful_data(self):
        pass
