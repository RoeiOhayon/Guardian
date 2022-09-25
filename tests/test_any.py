from guardian import guard
import pytest


# region None Guard Tests

def test_raises_if_none():
    with pytest.raises(ValueError):
        guard.none(None)


def test_not_raises_if_not_none():
    guard.none(object())


def test_decorator_raises_if_one_arg_is_none():
    @guard.none()
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function(1, 2, None)


def test_decorator_not_raises_if_no_arg_is_none():
    @guard.none()
    def function(a, b, c):
        return a or b or c

    function(1, 2, 3)


# endregion

# region Contains Guard Tests

def test_raises_if_contains():
    with pytest.raises(ValueError):
        guard.contains(["hello", "data"], "data")


def test_not_raises_if_not_contains():
    guard.contains(["hello", "not data"], "data")


def test_decorator_raises_if_one_arg_contains():
    @guard.contains("data")
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function([], ["hello"], ["not data", "data"])


def test_decorator_not_raises_if_no_arg_contains():
    @guard.contains("data")
    def function(a, b, c):
        return a or b or c

    function([], ["1"], ["2", "3"])


# endregion

# region Equals Guard Tests

def test_raises_if_equals():
    with pytest.raises(ValueError):
        guard.equals("data", "data")


def test_not_raises_if_not_equals():
    guard.equals("hello", "not hello")


def test_decorator_raises_if_one_arg_equals():
    @guard.equals("data")
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function(None, None, "data")


def test_decorator_not_raises_if_no_arg_equals():
    @guard.equals("data")
    def function(a, b, c):
        return a or b or c

    function([], "not data", 60)

# endregion
