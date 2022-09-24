from guardian._default_value import _DefaultValue
from guardian.guard import Guard

from typing import Optional, Callable, Sequence, Union
from numbers import Number


def zero(value: Number = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    Zero Guard
    :param value: Value to check if 0
    :return: If value is not provided, a decorator that checks all function's arguments will be returned
    """
    return Guard(value, "Zero", lambda v: v == 0, "Number cannot be 0", **kwargs)


def negative(value: Number = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    Negative Guard
    :param value: Value to check if negative
    :return: If value is not provided, a decorator that checks all function's arguments will be returned
    """
    return Guard(value, "Negative", lambda v: v < 0, "Number cannot be negative", **kwargs)


def not_negative(value: Number = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    Not Negative Guard
    :param value: Value to check if not negative
    :return: If value is not provided, a decorator that checks all function's arguments will be returned
    """
    return Guard(value, "NotNegative", lambda v: v >= 0, "Number must be negative", **kwargs)


def positive(value: Number = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    Positive Guard
    :param value: Value to check if positive
    :return: If value is not provided, a decorator that checks all function's arguments will be returned
    """
    return Guard(value, "Positive", lambda v: v > 0, "Number cannot be positive", **kwargs)


def not_positive(value: Number = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    Not Positive Guard
    :param value: Value to check not positive
    :return: If value is not provided, a decorator that checks all function's arguments will be returned
    """
    return Guard(value, "NotPositive", lambda v: v <= 0, "Number must be positive", **kwargs)


def in_range(value_or_range: Union[Number, Sequence[Number]] = _DefaultValue, rng: Sequence[Number] = _DefaultValue,
             **kwargs) -> \
        Optional[Callable]:
    """
    In Range Guard
    :param value_or_range:
        Value to check if in range, if range is not passed as second argument,
        the value will be treated as the range to check against
    :param rng: Range to check if value is in
    :return: If second parameter is not provided, a decorator that checks all function's arguments will be returned
    """
    if rng == _DefaultValue:
        rng, value_or_range = value_or_range, rng
    return Guard(value_or_range, "InRange", lambda v: rng[0] <= v <= rng[1], "Number cannot be in the specified range",
                 **kwargs)


def out_of_range(value_or_range: Union[Number, Sequence[Number]] = _DefaultValue,
                 rng: Sequence[Number] = _DefaultValue, **kwargs) -> \
        Optional[Callable]:
    """
    Out of Range Guard
    :param value_or_range:
        Value to check if out of range, if range is not passed as second argument,
        the value will be treated as the range to check against
    :param rng: Range to check if value is out of
    :return: If second parameter is not provided, a decorator that checks all function's arguments will be returned
    """
    if rng == _DefaultValue:
        rng, value_or_range = value_or_range, rng
    return Guard(value_or_range, "OutOfRange", lambda v: v > rng[1] or v < rng[0],
                 "Number cannot be outside the specified range", **kwargs)
