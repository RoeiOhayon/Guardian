from guardian.guard import Guard
from guardian._default_value import _DefaultValue
from typing import Optional, Callable
import re


def matches_regex(value_or_pattern: str = _DefaultValue, pattern: str = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    Matches Regex Guard
    :param value_or_pattern:
        Value to check if matches pattern, if pattern is not passed as second argument,
        the value will be treated as the pattern to check against
    :param pattern: Pattern to check if value is matching to
    :return: If second parameter is not provided, a decorator that checks all function's arguments will be returned
    """
    if pattern == _DefaultValue:
        pattern = value_or_pattern
        value_or_pattern = _DefaultValue
    return Guard(value_or_pattern, "MatchesRegex", lambda v: bool(re.match(pattern, v)),
                 "String must not match specified pattern", **kwargs)


def not_matches_regex(value_or_pattern: str = _DefaultValue, pattern: str = _DefaultValue, **kwargs) -> Optional[
    Callable]:
    """
    Not Matches Regex Guard
    :param value_or_pattern:
        Value to check if not matches pattern, if pattern is not passed as second argument,
        the value will be treated as the pattern to check against
    :param pattern: Pattern to check if value is not matching to
    :return: If second parameter is not provided, a decorator that checks all function's arguments will be returned
    """
    if pattern == _DefaultValue:
        pattern = value_or_pattern
        value_or_pattern = _DefaultValue
    return Guard(value_or_pattern, "NotMatchesRegex", lambda v: not re.match(pattern, v),
                 "String must match specified pattern", **kwargs)


def numeric(value: str = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    Numeric Guard
    :param value: Value to check if numeric
    :return: If value is not provided, a decorator that checks all function's arguments will be returned
    """
    return Guard(value, "Numeric", lambda v: v.isnumeric(), "String must not be numeric", **kwargs)


def not_numeric(value: str = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    Not Numeric Guard
    :param value: Value to check if not numeric
    :return: If value is not provided, a decorator that checks all function's arguments will be returned
    """
    return Guard(value, "NotNumeric", lambda v: not v.isnumeric(), "String must be numeric", **kwargs)


def alphabetic(value: str = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    Alphabetic Guard
    :param value: Value to check if alphabetic
    :return: If value is not provided, a decorator that checks all function's arguments will be returned
    """
    return Guard(value, "Alphabetic", lambda v: v.isalpha(), "String must not be alphabetic", **kwargs)


def not_alphabetic(value: str = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    Not Alphabetic Guard
    :param value: Value to check if not alphabetic
    :return: If value is not provided, a decorator that checks all function's arguments will be returned
    """
    return Guard(value, "NotAlphabetic", lambda v: not v.isalpha(), "String must be alphabetic", **kwargs)


def alphanumeric(value: str = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    Alphanumeric Guard
    :param value: Value to check if alphanumeric
    :return: If value is not provided, a decorator that checks all function's arguments will be returned
    """
    return Guard(value, "Alphanumeric", lambda v: v.isalnum(), "String must not be alphanumeric", **kwargs)


def not_alphanumeric(value: str = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    Not Alphanumeric Guard
    :param value: Value to check if not alphanumeric
    :return: If value is not provided, a decorator that checks all function's arguments will be returned
    """
    return Guard(value, "NotAlphanumeric", lambda v: not v.isalnum(), "String must be alphanumeric", **kwargs)


def whitespace(value: str = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    Whitespace Guard
    :param value: Value to check if whitespace
    :return: If value is not provided, a decorator that checks all function's arguments will be returned
    """
    return Guard(value, "Whitespace", lambda v: v.isspace(), "String must not be whitespace", **kwargs)


def lowercase(value: str = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    Lowercase Guard
    :param value: Value to check if lowercase
    :return: If value is not provided, a decorator that checks all function's arguments will be returned
    """
    return Guard(value, "Lowercase", lambda v: v.islower(), "String must not be lowercase", **kwargs)


def uppercase(value: str = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    Uppercase Guard
    :param value: Value to check if uppercase
    :return: If value is not provided, a decorator that checks all function's arguments will be returned
    """
    return Guard(value, "Uppercase", lambda v: v.isupper(), "String must not be uppercase", **kwargs)


def empty_or_whitespace(value: str = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    Empty or Whitespace Guard
    :param value: Value to check if empty or whitespace
    :return: If value is not provided, a decorator that checks all function's arguments will be returned
    """
    return Guard(value, "EmptyOrWhitespace", lambda v: v.isspace() or v == "", "String must not be empty or whitespace",
                 **kwargs)


def not_url(value: str = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    Not URL Guard
    :param value: Value to check if not URL
    :return: If value is not provided, a decorator that checks all function's arguments will be returned
    """
    pattern = r"^(https?|ftp|file)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]"

    return Guard(value, "NotURL", lambda v: not re.match(pattern, v), "String must be a valid URL", **kwargs)


def not_email(value: str = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    Not Email Guard
    :param value: Value to check if not URL
    :return: If value is not provided, a decorator that checks all function's arguments will be returned
    """
    pattern = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

    return Guard(value, "NotEmail", lambda v: not re.match(pattern, v), "String must be a valid email address",
                 **kwargs)


def not_ipv4(value: str = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    Not IPv4 Guard
    :param value: Value to check if not IPv4 address
    :return: If value is not provided, a decorator that checks all function's arguments will be returned
    """
    pattern = r"""^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$"""

    return Guard(value, "NotIPv4", lambda v: not re.match(pattern, v), "String must be a valid IPv4 address", **kwargs)


def not_base64(value: str = _DefaultValue, **kwargs) -> Optional[Callable]:
    """
    Not Base64 Guard
    :param value: Value to check if not Base64 encoded
    :return: If value is not provided, a decorator that checks all function's arguments will be returned
    """
    pattern = r"""^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$"""

    return Guard(value, "NotBase64", lambda v: not re.match(pattern, v), "String must be in Base64 encoding", **kwargs)
