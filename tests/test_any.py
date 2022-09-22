from guardian import guard
import pytest


def test_raises_when_none():
    with pytest.raises(ValueError):
        guard.none(None)


def test_decorator_raises_when_none():
    with pytest.raises(ValueError):
        @guard.none()
        def function(a, b, c):
            return a or b or c

        function(1, 2, None)


def test_raises_if_contains():
    with pytest.raises(ValueError):
        guard.contains(["data"], "data")


def test_decorator_raises_if_contains():
    with pytest.raises(ValueError):
        @guard.contains("data")
        def function(a, b, c):
            return a or b or c

        function([], [], ["data"])


def test_raises_if_equals():
    with pytest.raises(ValueError):
        guard.equals("data", "data")


def test_decorator_raises_if_equals():
    with pytest.raises(ValueError):
        @guard.equals("data")
        def function(a, b, c):
            return a or b or c

        function(None, None, "data")
