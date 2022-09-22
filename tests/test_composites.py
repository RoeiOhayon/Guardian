from guardian import guard
import pytest


@pytest.fixture()
def supported_types():
    return str, list, tuple, dict, set


def test_raises_when_empty(supported_types):
    for t in supported_types:
        with pytest.raises(ValueError):
            guard.empty(t())


def test_decorator_raises_when_empty(supported_types):
    @guard.empty()
    def function(a, b, c):
        return a or b or c

    for t in supported_types:
        with pytest.raises(ValueError):
            function(1, 2, t())
