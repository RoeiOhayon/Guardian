from guardian import Guard
import pytest


@pytest.fixture()
def custom_guard():
    return Guard("CustomGuard", lambda x: x["custom"] is None, "Custom Guard")


def test_custom_guard_raises(custom_guard):
    with pytest.raises(ValueError):
        custom_guard({"custom": None})


def test_decorator_custom_guard_raises(custom_guard):
    @custom_guard()
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function({"custom": True}, {"custom": True}, {"custom": None})
