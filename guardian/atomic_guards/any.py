from guardian.guard import Guard
from guardian._default_value import _DefaultValue
from typing import Optional, Callable


def none(value: any = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    None Guard
    :param value: Value to check if None
    :return: If value is not provided, a decorator that checks all function's arguments will be returned
    """
    return Guard(value, "None", lambda v: v is None, "Value must not be None", **kwargs)


def contains(value_or_element: any = _DefaultValue, element: any = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    Contains Guard
    :param value_or_element:
        Value to check if contains element, if element is not passed as second argument,
        the value will be treated as the element to search
    :param element: Element to search
    :return: If second parameter is not provided, a decorator that checks all function's arguments will be returned
    """
    if element == _DefaultValue:
        element, value_or_element = value_or_element, element
    return Guard(value_or_element, "Contains", lambda v: element in v,
                 "Element must not be contained in provided value", **kwargs)


def equals(value_or_element: any = _DefaultValue, element: any = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    Equals Guard
    :param value_or_element:
        Value to check if equals to element, if element is not passed as second argument,
        the value will be treated as the element to check equality to
    :param element: Element to check equality to
    :return: If second parameter is not provided, a decorator that checks all function's arguments will be returned
    """
    if element == _DefaultValue:
        element, value_or_element = value_or_element, element
    return Guard(value_or_element, "Equals", lambda v: v == element, "Element must not be equal to provided value",
                 **kwargs)
