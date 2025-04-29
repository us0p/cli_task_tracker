import pytest
from typing import cast, List
from uuid import uuid4
from random import choice
from datetime import datetime, UTC
from unittest.mock import Mock

import tabulate

from src.application.mappers.task import TaskDict
from src.domain.entities.task.task import TaskStatus
from src.interfaces.cli.cli_displayer import CLITabulator


class TaskDictFaker:
    def __init__(self):
        today = datetime.now(UTC)
        self.id = uuid4().hex
        self.status = choice(seq=["todo", "done", "in-progress"])
        self.description = "description"
        self.createdAt = today.isoformat()
        self.updatedAt = today.isoformat()

    def get_dict(self) -> TaskDict:
        return {
            "id": self.id,
            "status": cast(TaskStatus, self.status),
            "description": self.description,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
        }


class TestCLIDisplayer:
    def setup_method(self):
        self.data: List[TaskDict] = []
        for _ in range(10):
            fake = TaskDictFaker()
            self.data.append(fake.get_dict())

    def _assert_date_format(self, date: str, format: str) -> bool:
        try:
            datetime.strptime(date, format)
            return True
        except ValueError:
            return False

    def test_user_readable_information(self):
        task = self.data[0]
        cli_displayer = CLITabulator(task)
        user_readable_information = (
            cli_displayer._get_user_readable_information(task)
        )

        assert len(user_readable_information["id"]) == 5

        assert user_readable_information["status"] in [
            "todo",
            "done",
            "in-progress",
        ]

        assert user_readable_information["description"] == "description"

        assert (
            self._assert_date_format(
                str(user_readable_information.get("updatedAt")),
                "%m/%d/%Y - %H:%M",
            )
            is True
        )

        assert user_readable_information.get("createdAt") is None

    def test_information_parser_applied_to_display(
        self, monkeypatch: pytest.MonkeyPatch
    ):
        tabulate_fn = Mock(return_value="")
        monkeypatch.setattr(tabulate, "tabulate", tabulate_fn)

        cli_displayer = CLITabulator(self.data)
        cli_displayer._get_user_readable_information = Mock(
            return_value=self.data[0]
        )

        cli_displayer.tabulate()

        assert (
            cli_displayer._get_user_readable_information.call_count
            == len(self.data)
        )

        tabulate_fn.assert_called_once_with(
            [self.data[0]] * len(self.data), headers="keys"
        )
