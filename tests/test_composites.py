from guardian import guard
from guardian.atomic_guards.composites import composites_supported_types
import pytest


@pytest.fixture()
def supported_types():
    return composites_supported_types


def test_raises_if_empty(supported_types):
    for t in supported_types:
        with pytest.raises(ValueError):
            guard.empty(t())


def test_not_raises_if_not_empty(supported_types):
    for t in supported_types:
        guard.empty(t({"key": "value"}))


def test_decorator_raises_if_one_arg_is_empty(supported_types):
    @guard.empty()
    def function(a, b, c):
        return a or b or c

    for t in supported_types:
        with pytest.raises(ValueError):
            function(1, [1, 2], t())


def test_decorator_not_raises_if_no_arg_is_empty(supported_types):
    @guard.empty()
    def function(a, b, c):
        return a or b or c

    for t in supported_types:
        function(1, [2, 3], t({"key": "value"}))
