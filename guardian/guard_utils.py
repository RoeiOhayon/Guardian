import inspect
from typing import Callable
from guardian._default_value import _DefaultValue


def get_arg_count(func):
    return len(inspect.getfullargspec(func).args)


def is_validation_call(predicate: Callable[..., bool], arguments) -> bool:
    return _DefaultValue not in arguments and len(arguments) == get_arg_count(predicate)


def transform_argument(argument, kwargs):
    if "property" in kwargs:
        return getattr(argument, kwargs["property"])
    elif "key" in kwargs:
        return argument[kwargs["key"]]
    elif "transformer" in kwargs:
        return kwargs["transformer"](argument)
    else:
        return argument
