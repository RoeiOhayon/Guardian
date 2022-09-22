from guardian.guard import Guard
from guardian._default_value import _DefaultValue
from typing import Optional, Callable


def none(value: any = _DefaultValue) -> Optional[Callable]:
    """
    None Guard
    :param value: Value to check
    :return: If value is is not initialized, a decorator that checks all arguments will be returned
    """
    return Guard(value, "None", lambda v: v is None, "Value must not be None")


def contains(value_or_element: any = _DefaultValue, element: any = _DefaultValue) -> Optional[Callable]:
    """
    Contains Guard
    :param value_or_element: Value to check
    :param element: Specified element
    :return: If value is not initialized, a decorator that checks all arguments will be returned
    """
    if element == _DefaultValue:
        element = value_or_element
        value_or_element = _DefaultValue
    return Guard(value_or_element, "Contains", lambda v: element in v, "Element must not be inside provided value")


def equals(value_or_element: any = _DefaultValue, element: any = _DefaultValue) -> Optional[Callable]:
    """
    Contains Guard
    :param value_or_element: Value to check
    :param element: Specified element
    :return: If value is not initialized, a decorator that checks all arguments will be returned
    """
    if element == _DefaultValue:
        element = value_or_element
        value_or_element = _DefaultValue
    return Guard(value_or_element, "Equals", lambda v: v == element, "Element must not be equal to provided value")
