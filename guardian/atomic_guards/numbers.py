from guardian._default_value import _DefaultValue
from guardian.guard import Guard

from typing import Optional, Callable, Sequence, Union
from numbers import Number
from math import inf


def zero(value: Number = _DefaultValue) -> Optional[Callable]:
    """
    Zero Guard
    :param value: Value to check
    :return: If value is not initialized, a decorator that checks all arguments will be returned
    """
    return Guard(value, "Zero", lambda v: v == 0, "Number cannot be 0")


def negative(value: Number = _DefaultValue) -> Optional[Callable]:
    """
    Negative Guard
    :param value: Value to check
    :return: If value is not initialized, a decorator that checks all arguments will be returned
    """
    return Guard(value, "Negative", lambda v: v < 0, "Number cannot be negative")


def not_negative(value: Number = _DefaultValue) -> Optional[Callable]:
    """
    Not Negative Guard
    :param value: Value to check
    :return: If value is not initialized, a decorator that checks all arguments will be returned
    """
    return Guard(value, "NotNegative", lambda v: v >= 0, "Number must be negative")


def positive(value: Number = _DefaultValue) -> Optional[Callable]:
    """
    Positive Guard
    :param value: Value to check
    :return: If value is not initialized, a decorator that checks all arguments will be returned
    """
    return Guard(value, "Positive", lambda v: v > 0, "Number cannot be positive")


def not_positive(value: Number = _DefaultValue) -> Optional[Callable]:
    """
    Not Positive Guard
    :param value: Value to check
    :return: If value is not initialized, a decorator that checks all arguments will be returned
    """
    return Guard(value, "NotPositive", lambda v: v <= 0, "Number must be positive")


def in_range(value_or_range: Union[Number, Sequence[Number]] = _DefaultValue, rng: Sequence[Number] = _DefaultValue) -> \
        Optional[Callable]:
    """
    In Range Guard
    :param value_or_range: Value to check, if it's a range a that checks all arguments will be returned
    :param rng: Specified range (Initialized only if value_or_range is a Number)
    :return: If value is not initialized, a decorator that checks all arguments will be returned
    """
    if rng == _DefaultValue:
        rng = value_or_range
        value_or_range = _DefaultValue
    return Guard(value_or_range, "InRange", lambda v: rng[0] <= v <= rng[1],
                 "number cannot be in the specified range")


def out_of_range(value_or_range: Union[Number, Sequence[Number]] = _DefaultValue,
                 rng: Sequence[Number] = _DefaultValue) -> \
        Optional[Callable]:
    """
    Out Range Guard
    :param value_or_range: Value to check, if it's a range a that checks all arguments will be returned
    :param rng: Specified range (Initialized only if value_or_range is a Number)
    :return: If value is not initialized, a decorator that checks all arguments will be returned
    """
    if rng == _DefaultValue:
        rng = value_or_range
        value_or_range = _DefaultValue
    return Guard(value_or_range, "OutOfRange", lambda v: v > rng[1] or v < rng[0],
                 "number cannot be outside the specified range")
