from guardian import guard
import pytest


def test_raises_if_zero():
    with pytest.raises(ValueError):
        guard.zero(0)


def test_decorator_raises_if_zero():
    @guard.zero()
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function(99, 99, 0)
