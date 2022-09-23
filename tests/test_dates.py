from guardian import guard
import pytest


@pytest.fixture()
def date_range():
    return -10, 10


def test_raises_when_in_date_range(date_range):
    with pytest.raises(ValueError):
        guard.in_date_range(0, date_range)


def test_decorator_raises_when_in_date_range(date_range):
    @guard.in_date_range(date_range)
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function(-99, -99, 0)


def test_raises_if_out_of_date_range(date_range):
    with pytest.raises(ValueError):
        guard.out_of_date_range(99, date_range)


def test_decorator_raises_if_one_arg_out_of_date_range(date_range):
    @guard.out_of_date_range(date_range)
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function(0, 0, 99)


def test_raises_if_before():
    with pytest.raises(ValueError):
        guard.before(0, 10)


def test_decorator_raises_if_before():
    @guard.before(10)
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function(99, 99, -99)


def test_raises_if_after():
    with pytest.raises(ValueError):
        guard.after(99, 10)


def test_decorator_raises_if_one_arg_after():
    @guard.after(10)
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function(-99, -99, 99)
