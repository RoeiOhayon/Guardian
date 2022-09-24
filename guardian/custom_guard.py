from guardian._default_value import _DefaultValue
from guardian.guard_utils import is_validation_call, transform_argument

from typing import Callable
from functools import wraps


class CustomGuard:
    def __new__(cls, name: str, predicate: Callable[..., bool], description: str):
        def guard_decorator(*args, **kwargs):
            if is_validation_call(predicate, args):
                if predicate(*args):
                    raise ValueError(f"Guardian.{name} Guard: {description}")
                return
            else:
                def guarded_func_decorator(func):
                    @wraps(func)
                    def guarded_function(*inner_args, **inner_kwargs):
                        for arg in inner_args:
                            arg = transform_argument(arg, kwargs)
                            args_without_default_value = [a for a in args if a != _DefaultValue]
                            if predicate(arg, *args_without_default_value):
                                raise ValueError(f"Guardian.{name} Guard: {description}")
                        return func(*inner_args, **inner_kwargs)

                    return guarded_function
            return guarded_func_decorator

        return guard_decorator
