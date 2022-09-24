from guardian import Guard
import pytest


@pytest.fixture()
def custom_guard():
    return Guard("CustomGuard", lambda v, r: v["custom"] == r, f"value['custom'] cannot be equal to parameter")


def test_custom_guard_raises_if_qualifies(custom_guard):
    with pytest.raises(ValueError):
        custom_guard({"custom": 99}, 99)


def test_custom_guard_not_raises_if_not_qualifies(custom_guard):
    custom_guard({"custom": 99}, "hello")


def test_decorator_custom_guard_raises_if_one_arg_qualifies(custom_guard):
    @custom_guard(99)
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function({"custom": False}, {"custom": "hello"}, {"custom": 99})


def test_decorator_custom_guard_not_raises_if_no_arg_qualifies(custom_guard):
    @custom_guard(99)
    def function(a, b, c):
        return a or b or c

    function({"custom": False}, {"custom": "hello"}, {"custom": True})
