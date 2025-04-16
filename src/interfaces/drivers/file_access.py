from os.path import exists, join, realpath
from json import dumps


class JsonDB:
    def __init__(self):
        self._file_name = realpath(
            join(__file__, "..", "..", "..", "db.json")
        )

        valid_file_name = exists(self._file_name)

        if not valid_file_name:
            with open(self._file_name, "w") as f:
                f.write(dumps([]))
