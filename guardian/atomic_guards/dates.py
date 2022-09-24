from guardian.guard import Guard
from guardian._default_value import _DefaultValue

from typing import Union, Sequence, Optional, Callable
from numbers import Number


def in_date_range(value_or_range: Union[float, Sequence[float]] = _DefaultValue,
                  rng: Sequence[float] = _DefaultValue, **kwargs) -> [Callable]:
    """
    In Date Range Guard
    :param value_or_range:
        Value to check if in date range, if date range is not passed as second argument,
        the value will be treated as the date range to check against
    :param rng: Range to check if date is in
    :return: If second parameter is not provided, a decorator that checks all function's arguments will be returned
    """
    if rng == _DefaultValue:
        rng, value_or_range = value_or_range, rng
    return Guard(value_or_range, "InDateRange", lambda v: rng[0] <= v <= rng[1],
                 "Date cannot be in the specified range", **kwargs)


def out_of_date_range(value_or_range: Union[float, Sequence[Number]] = _DefaultValue,
                      rng: Sequence[float] = _DefaultValue, **kwargs) -> \
        Optional[Callable]:
    """
    Out of Date Range Guard
    :param value_or_range:
        Value to check if out of date range, if date range is not passed as second argument,
        the value will be treated as the date range to check against
    :param rng: Range to check if date is out of
    :return: If second parameter is not provided, a decorator that checks all function's arguments will be returned
    """
    if rng == _DefaultValue:
        rng, value_or_range = value_or_range, rng
    return Guard(value_or_range, "OutOfDateRange", lambda v: v > rng[1] or v < rng[0],
                 "Date cannot be out of the specified range", **kwargs)


def after(value_or_min_date: float = _DefaultValue, min_date: float = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    After Guard
    :param value_or_min_date:
        Value to check if is after minimum date,
        if min_date is not passed as second argument, the value will be treated as the minimum date to check against
    :param min_date: Minimum date to check if value is after
    :return: If second parameter is not provided, a decorator that checks all function's arguments will be returned
    """
    if min_date == _DefaultValue:
        min_date, value_or_min_date = value_or_min_date, min_date
    return Guard(value_or_min_date, "AfterDate", lambda v: v > min_date, "Date must be before specified date", **kwargs)


def before(value_or_max_date: float = _DefaultValue, max_date: float = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    Before Guard
    :param value_or_max_date:
        Value to check if is before maximum date, if max_date is not passed as second argument,
        the value will be treated as the maximum date to check against
    :param max_date: Maximum date to check if value is before
    :return: If second parameter is not provided, a decorator that checks all function's arguments will be returned
    """
    if max_date == _DefaultValue:
        max_date, value_or_max_date = value_or_max_date, max_date
    return Guard(value_or_max_date, "BeforeDate", lambda v: v < max_date, "Date must be after specified date", **kwargs)
