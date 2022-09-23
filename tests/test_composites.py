from guardian import guard
import pytest


@pytest.fixture()
def supported_types():
    return str, list, tuple, dict, set


def test_raises_if_empty(supported_types):
    for t in supported_types:
        with pytest.raises(ValueError):
            guard.empty(t())


def test_decorator_raises_if_one_arg_empty(supported_types):
    @guard.empty()
    def function(a, b, c):
        return a or b or c

    for t in supported_types:
        with pytest.raises(ValueError):
            function(1, 2, t())
