import pytest

from src.domain.entities.task.task import Task
from src.domain.errors.validation import ValidationError


class TestTaskEntity:
    
    @pytest.mark.parametrize(
        "task",
        [
            {},
            {"status": "some status"},
        ],
    )
    def test_validate_fails_for_bad_data(self, task):
        entity = Task(task.get("status"))

        with pytest.raises(ValidationError):
            entity.validate()


    def test_validation_success(self):
        entity = Task("done")
        try:
            entity.validate()
        except Exception as e:
            pytest.fail(f"Unexpected exception raised: {e}")
