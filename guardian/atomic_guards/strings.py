from guardian.guard import Guard
from guardian._default_value import _DefaultValue
from typing import Optional, Callable
import re


def matches_regex(value_or_pattern: str = _DefaultValue, pattern: str = _DefaultValue) -> Optional[Callable]:
    """
    Matches Regex Guard
    :param value_or_pattern: Value to check, if it's a pattern a that checks all arguments will be returned
    :param pattern: Specified pattern
    :return: If value is not initialized, a decorator that checks all arguments will be returned
    """
    if pattern == _DefaultValue:
        pattern = value_or_pattern
        value_or_pattern = _DefaultValue
    return Guard(value_or_pattern, "MatchesRegex", lambda v: bool(re.match(pattern, v)),
                 "String must not match specified pattern")


def not_matches_regex(value_or_pattern: str = _DefaultValue, pattern: str = _DefaultValue) -> Optional[Callable]:
    """
    Not Matches Regex Guard
    :param value_or_pattern: Value to check, if it's a pattern a that checks all arguments will be returned
    :param pattern: Specified pattern
    :return: If value is not initialized, a decorator that checks all arguments will be returned
    """
    if pattern == _DefaultValue:
        pattern = value_or_pattern
        value_or_pattern = _DefaultValue
    return Guard(value_or_pattern, "NotMatchesRegex", lambda v: not re.match(pattern, v),
                 "String match specified pattern")


def numeric(value: str = _DefaultValue) -> Optional[Callable]:
    """
    Numeric Guard
    :param value: Value to check
    :return: If value is is not initialized, a decorator that checks all arguments will be returned
    """
    return Guard(value, "Numeric", lambda v: v.isnumeric(), "String must not be numeric")


def not_numeric(value: str = _DefaultValue) -> Optional[Callable]:
    """
    Not Numeric Guard
    :param value: Value to check
    :return: If value is is not initialized, a decorator that checks all arguments will be returned
    """
    return Guard(value, "NotNumeric", lambda v: not v.isnumeric(), "String must be numeric")


def alphabetic(value: str = _DefaultValue) -> Optional[Callable]:
    """
    Alphabetic Guard
    :param value: Value to check
    :return: If value is is not initialized, a decorator that checks all arguments will be returned
    """
    return Guard(value, "Alphabetic", lambda v: v.isalpha(), "String must not be alphabetic")


def not_alphabetic(value: str = _DefaultValue) -> Optional[Callable]:
    """
    Not Alphabetic Guard
    :param value: Value to check
    :return: If value is is not initialized, a decorator that checks all arguments will be returned
    """
    return Guard(value, "NotAlphabetic", lambda v: not v.isalpha(), "String must be alphabetic")


def alphanumeric(value: str = _DefaultValue) -> Optional[Callable]:
    """
    Alphanumeric Guard
    :param value: Value to check
    :return: If value is is not initialized, a decorator that checks all arguments will be returned
    """
    return Guard(value, "Alphanumeric", lambda v: v.isalnum(), "String must not be alphanumeric")


def not_alphanumeric(value: str = _DefaultValue) -> Optional[Callable]:
    """
    Not Alphanumeric Guard
    :param value: Value to check
    :return: If value is is not initialized, a decorator that checks all arguments will be returned
    """
    return Guard(value, "NotAlphanumeric", lambda v: not v.isalnum(), "String must be alphanumeric")


def whitespace(value: str = _DefaultValue) -> Optional[Callable]:
    """
    Whitespace Guard
    :param value: Value to check
    :return: If value is is not initialized, a decorator that checks all arguments will be returned
    """
    return Guard(value, "Whitespace", lambda v: v.isspace(), "String must not be whitespace")


def lowercase(value: str = _DefaultValue) -> Optional[Callable]:
    """
    Lowercase Guard
    :param value: Value to check
    :return: If value is is not initialized, a decorator that checks all arguments will be returned
    """
    return Guard(value, "Lowercase", lambda v: v.islower(), "String must not be lowercase")


def uppercase(value: str = _DefaultValue) -> Optional[Callable]:
    """
    Uppercase Guard
    :param value: Value to check
    :return: If value is is not initialized, a decorator that checks all arguments will be returned
    """
    return Guard(value, "Uppercase", lambda v: v.isupper(), "String must not be uppercase")
