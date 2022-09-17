from guardian.guard import Guard
from guardian._default_value import _DefaultValue

from typing import Callable, Optional


def none(value: any = _DefaultValue) -> Optional[Callable]:
    """
    None Guard
    :param value: Value to check
    :return: If value is None, a decorator that checks all arguments will be returned
    """
    return Guard(value, "None", lambda v: v is None, "Value must not be None")
