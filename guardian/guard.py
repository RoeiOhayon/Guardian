import re


def _guard_arguments(value, predicate, value_description):
    if callable(value):
        def wrapped(*args, **kwargs):
            for arg in args:
                if predicate(arg):
                    raise ValueError(f"Guardian: {value_description} Argument is Not Allowed")
            return value(*args, **kwargs)

        return wrapped
    else:
        if predicate(value):
            raise ValueError(f"Guardian: {value_description} Argument is Not Allowed")


def none(value):
    return _guard_arguments(value, lambda x: x is None, "None")


def negative(value):
    return _guard_arguments(value, lambda x: x < 0, "Negative")


def zero(value):
    return _guard_arguments(value, lambda x: x == 0, "Zero")


def positive(value):
    return _guard_arguments(value, lambda x: x > 0, "Positive")


def out_of_range(wanted_range, value=None):
    if value:
        return _guard_arguments(value, lambda x: x > wanted_range[1] or x < wanted_range[0], "Not in Range")
    else:
        def wrapped(func):
            return _guard_arguments(func, lambda x: x > wanted_range[1] or x < wanted_range[0], "Not in Range")

        return wrapped


def regex(pattern, value=None):
    if value:
        return _guard_arguments(value, lambda x: not re.match(pattern, x), "Unmatched Regex Pattern")
    else:
        def wrapped(func):
            return _guard_arguments(func, lambda x: not re.match(pattern, x), "Unmatched Regex Pattern")

        return wrapped


def not_numeric(value):
    return _guard_arguments(value, lambda x: not x.isnumeric(), "Not Numeric")


def not_alphabetic(value):
    return _guard_arguments(value, lambda x: not x.isalpha(), "Not Alphabetic")


def not_alphanumeric(value):
    return _guard_arguments(value, lambda x: not x.isalnum(), "Not AlphaNumeric")
