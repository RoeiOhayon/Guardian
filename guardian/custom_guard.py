from guardian._default_value import _DefaultValue

from typing import Callable
import inspect
from functools import wraps


def get_arg_count(func):
    return len(inspect.getfullargspec(func).args)


class CustomGuard:
    def __new__(cls, name: str, predicate: Callable[..., bool], description: str):
        def guard_decorator(*args):
            if len(args) == get_arg_count(predicate) and _DefaultValue not in args:
                if predicate(*args):
                    raise ValueError(f"Guardian.{name} Guard: {description}")
                return
            else:
                def guarded_func_decorator(func):
                    @wraps(func)
                    def guarded_function(*inner_args, **kwargs):
                        for arg in inner_args:
                            args_without_default_value = [a for a in args if a != _DefaultValue]
                            if predicate(arg, *args_without_default_value):
                                raise ValueError(f"Guardian.{name} Guard: {description}")
                        return func(*inner_args, **kwargs)

                    return guarded_function
            return guarded_func_decorator

        return guard_decorator
