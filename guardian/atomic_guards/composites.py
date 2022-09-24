from guardian.guard import Guard
from guardian._default_value import _DefaultValue
from typing import Optional, Callable, Union

composites_supported_types = str, list, tuple, dict, set


def empty(value: Union[composites_supported_types] = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    Empty Guard
    :param value: Value to check if empty
    :return: If value is not provided, a decorator that checks all function's arguments will be returned
    """
    return Guard(value, "Empty", lambda v: v == "" or v == [] or v == () or v == {} or v == set(),
                 "Value must not be empty", **kwargs)
