from os.path import exists, join, realpath
from json import dumps


class JsonDB:
    def __init__(self, file_name="db.json"):
        self._file_name = realpath(
            join(__file__, "..", "..", "..", "..", file_name)
        )

        valid_file_name = exists(self._file_name)

        if not valid_file_name:
            with open(self._file_name, "w") as f:
                f.write(dumps([]))
