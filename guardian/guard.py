from typing import Callable
import inspect
from functools import wraps


def get_arg_count(func):
    return len(inspect.getfullargspec(func).args)


class Guard:
    def __new__(cls, name: str, predicate: Callable[..., bool], description: str):
        def guard_decorator(*args):
            if len(args) == get_arg_count(predicate):
                return predicate(*args)
            else:
                def guarded_func_decorator(func):
                    @wraps(func)
                    def guarded_function(*inner_args, **kwargs):
                        for arg in inner_args:
                            if predicate(arg, *args):
                                raise ValueError(f"Guardian: {name} {description} Argument is Not Allowed")
                        return func(*inner_args, **kwargs)

                    return guarded_function
            return guarded_func_decorator

        return guard_decorator
