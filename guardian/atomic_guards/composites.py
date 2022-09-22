from guardian.guard import Guard
from guardian._default_value import _DefaultValue
from typing import Optional, Callable, Union


def empty(value: Union[str, list, tuple, dict, set] = _DefaultValue) -> Optional[Callable]:
    """
    Empty Guard
    :param value: Value to check
    :return: If value is is not initialized, a decorator that checks all arguments will be returned
    """
    return Guard(value, "Empty", lambda v: v == "" or v == [] or v == () or v == {} or v == set(),
                 "Value must not be empty")
