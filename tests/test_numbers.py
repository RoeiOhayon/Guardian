from guardian import guard
import pytest


# region Zero Guard Tests

def test_raises_if_zero():
    with pytest.raises(ValueError):
        guard.zero(0)


def test_not_raises_if_not_zero():
    guard.zero(99)


def test_decorator_raises_if_one_arg_is_zero():
    @guard.zero()
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function(99, 99, 0)


def test_decorator_not_raises_if_no_arg_is_zero():
    @guard.zero()
    def function(a, b, c):
        return a or b or c

    function(1, 2, 3)


# endregion

# region Negative Guard Tests

def test_raises_if_negative():
    with pytest.raises(ValueError):
        guard.negative(-99)


def test_not_raises_if_not_negative():
    guard.negative(0)
    guard.negative(1)


def test_decorator_raises_if_one_arg_is_negative():
    @guard.negative()
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function(0, 99, -99)


def test_decorator_not_raises_if_no_arg_is_negative():
    @guard.negative()
    def function(a, b, c):
        return a or b or c

    function(0, 1, 2)


# endregion

# region Positive Guard Tests

def test_raises_if_positive():
    with pytest.raises(ValueError):
        guard.positive(99)


def test_not_raises_if_not_positive():
    guard.positive(0)
    guard.positive(-1)


def test_decorator_raises_if_one_arg_is_positive():
    @guard.positive()
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function(0, -99, 99)


def test_decorator_not_raises_if_no_arg_is_positive():
    @guard.positive()
    def function(a, b, c):
        return a or b or c

    function(0, -1, -2)


# endregion

# region NotNegative Guard Tests

def test_raises_if_not_negative():
    with pytest.raises(ValueError):
        guard.not_negative(0)
    with pytest.raises(ValueError):
        guard.not_negative(1)


def test_not_raises_if_not_not_negative():
    guard.not_negative(-99)


def test_decorator_raises_if_one_arg_is_not_negative():
    @guard.not_negative()
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function(-99, -99, 0)
    with pytest.raises(ValueError):
        function(-99, -99, 1)


def test_decorator_not_raises_if_no_arg_is_not_negative():
    @guard.not_negative()
    def function(a, b, c):
        return a or b or c

    function(-1, -2, -3)


# endregion

# region NotPositive Guard Tests

def test_raises_if_not_positive():
    with pytest.raises(ValueError):
        guard.not_positive(0)
    with pytest.raises(ValueError):
        guard.not_positive(-1)


def test_not_raises_if_not_not_positive():
    guard.not_positive(99)


def test_decorator_raises_if_one_arg_is_not_positive():
    @guard.not_positive()
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function(99, 99, 0)
    with pytest.raises(ValueError):
        function(99, 99, -1)


def test_decorator_not_raises_if_no_arg_is_not_positive():
    @guard.not_positive()
    def function(a, b, c):
        return a or b or c

    function(1, 2, 3)


# endregion

@pytest.fixture()
def number_range():
    return -10, 10


# region InRange Guard Tests


def test_raises_if_in_range(number_range):
    with pytest.raises(ValueError):
        guard.in_range(0, number_range)


def test_not_raises_if_not_in_range(number_range):
    guard.in_range(99, number_range)


def test_decorator_raises_if_one_args_is_in_range(number_range):
    @guard.in_range(number_range)
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function(-99, 99, 0)


def test_decorator_not_raises_if_no_arg_is_in_range(number_range):
    @guard.in_range(number_range)
    def function(a, b, c):
        return a or b or c

    function(99, -99, 99)


# endregion

# region InRange Guard Tests

def test_raises_if_out_of_range(number_range):
    with pytest.raises(ValueError):
        guard.out_of_range(99, number_range)


def test_not_raises_if_not_out_of_range(number_range):
    guard.out_of_range(0, number_range)


def test_decorator_raises_if_one_args_is_out_of_range(number_range):
    @guard.out_of_range(number_range)
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function(-1, 1, 99)


def test_decorator_not_raises_if_no_arg_is_out_of_range(number_range):
    @guard.out_of_range(number_range)
    def function(a, b, c):
        return a or b or c

    function(-1, 1, 0)

# endregion
