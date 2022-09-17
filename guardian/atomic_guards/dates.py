from guardian.guard import Guard
from guardian._default_value import _DefaultValue

from typing import Union, Sequence, Optional, Callable
from numbers import Number
from math import inf


def in_date_range(value_or_range: Union[Number, Sequence[Number]] = _DefaultValue,
                  rng: Sequence[Number] = _DefaultValue) -> \
        Optional[Callable]:
    """
    In Date Range Guard
    :param value_or_range: Value to check, if it's a range a that checks all arguments will be returned
    :param rng: Specified range (Initialized only if value_or_range is a Number)
    :return: If value is not initialized, a decorator that checks all arguments will be returned
    """
    if rng == _DefaultValue:
        rng = value_or_range
        value_or_range = _DefaultValue
    return Guard(value_or_range, "InDateRange", lambda v: rng[0] <= v <= rng[1],
                 "Date cannot be in the specified range")


def out_of_date_range(value_or_range: Union[Number, Sequence[Number]] = _DefaultValue,
                      rng: Sequence[Number] = _DefaultValue) -> \
        Optional[Callable]:
    """
    Out of Date Range Guard
    :param value_or_range: Value to check, if it's a range a that checks all arguments will be returned
    :param rng: Specified range (Initialized only if value_or_range is a Number)
    :return: If value is not initialized, a decorator that checks all arguments will be returned
    """
    if rng == _DefaultValue:
        rng = value_or_range
        value_or_range = _DefaultValue
    return Guard(value_or_range, "OutOfDateRange", lambda v: v > rng[1] or v < rng[0],
                 "Date cannot be outside the specified range")


def after(value_or_min_date: Union[float, Sequence[float]] = _DefaultValue,
          min_date: Sequence[float] = _DefaultValue) -> \
        Optional[Callable]:
    """
    After Guard
    :param value_or_min_date: Value to check, if it's a range a that checks all arguments will be returned
    :param min_date: Specified date (Initialized only if value_or_min_date is a float)
    :return: If value is not initialized, a decorator that checks all arguments will be returned
    """
    if min_date == _DefaultValue:
        min_date = value_or_min_date
        value_or_min_date = _DefaultValue
    return Guard(value_or_min_date, "AfterDate", lambda v: v > min_date, "Date must be before specified date")


def before(value_or_max_date: Union[float, Sequence[float]] = _DefaultValue,
           max_date: Sequence[float] = _DefaultValue) -> \
        Optional[Callable]:
    """
    After Guard
    :param value_or_max_date: Value to check, if it's a range a that checks all arguments will be returned
    :param max_date: Specified date (Initialized only if value_or_min_date is a float)
    :return: If value is not initialized, a decorator that checks all arguments will be returned
    """
    if max_date == _DefaultValue:
        max_date = value_or_max_date
        value_or_max_date = _DefaultValue
    return Guard(value_or_max_date, "BeforeDate", lambda v: v < max_date, "Date must be after specified date")
