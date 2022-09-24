from guardian import Guard
import pytest
from dataclasses import dataclass


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


@dataclass
class Person:
    data: dict


def test_decorator_custom_guard_raises_if_one_arg_extracted_property_qualifies(custom_guard):
    @custom_guard(99, property="data")
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function(Person({"custom": False}), Person({"custom": "hello"}), Person({"custom": 99}))


def test_decorator_custom_guard_not_raises_if_no_arg_extracted_property_qualifies(custom_guard):
    @custom_guard(99, property="data")
    def function(a, b, c):
        return a or b or c

    function(Person({"custom": False}), Person({"custom": "hello"}), Person({"custom": True}))


def test_decorator_custom_guard_raises_if_one_arg_transformed_qualifies(custom_guard):
    @custom_guard(99, transformer=lambda v: v.data)
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function(Person({"custom": False}), Person({"custom": "hello"}), Person({"custom": 99}))


def test_decorator_custom_guard_not_raises_if_no_arg_transformed_qualifies(custom_guard):
    @custom_guard(99, transformer=lambda v: v.data)
    def function(a, b, c):
        return a or b or c

    function(Person({"custom": False}), Person({"custom": "hello"}), Person({"custom": True}))


def test_decorator_custom_guard_raises_if_one_arg_value_at_key_qualifies(custom_guard):
    @custom_guard(99, key="data")
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function({"data": {"custom": False}}, {"data": {"custom": "hello"}}, {"data": {"custom": 99}})


def test_decorator_custom_guard_not_raises_if_no_arg_value_at_key_qualifies(custom_guard):
    @custom_guard(99, key="data")
    def function(a, b, c):
        return a or b or c

    function({"data": {"custom": False}}, {"data": {"custom": "hello"}}, {"data": {"custom": True}})
