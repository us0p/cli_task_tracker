from datetime import datetime
from typing import Union, List

import tabulate

from src.application.mappers.task import TaskDict


# Test this class to display only relevant information
class CLITabulator:
    def __init__(self, data: Union[TaskDict, List[TaskDict], str]):
        self.data = data

    def tabulate(self) -> str:
        if type(self.data) is dict:
            return tabulate.tabulate(
                [self._get_user_readable_information(self.data)],
                headers="keys",
            )

        if type(self.data) is list:
            return tabulate.tabulate(
                [
                    self._get_user_readable_information(t)
                    for t in self.data
                ],
                headers="keys",
            )

        return str(self.data)

    def _get_user_readable_information(self, data: TaskDict):
        date = datetime.fromisoformat(data["updatedAt"])
        return {
            "id": data["id"][0:5],
            "status": data["status"],
            "description": data["description"],
            "updatedAt": date.strftime("%m/%d/%Y - %H:%M"),
        }
