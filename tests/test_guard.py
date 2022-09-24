import pytest

from guardian import guard
from dataclasses import dataclass
from typing import Optional


def test_decorator_not_raises_if_zero_args():
    @guard.none()
    def function():
        return "Hi Everyone"

    function()


@dataclass
class Person:
    name: Optional[str]


# region ExtractProperty Tests

def test_decorator_raises_if_extracted_property_is_none():
    @guard.none(property="name")
    def function(person):
        return "name: " + person.name

    with pytest.raises(ValueError):
        function(Person(None))


def test_decorator_not_raises_if_extracted_property_is_not_none():
    @guard.none(property="name")
    def function(person):
        return "name: " + person.name

    function(Person("John"))


def test_decorator_raises_if_extracted_property_matches_regex():
    @guard.matches_regex(".*el$", property="name")
    def function(person):
        return "name: " + person.name

    with pytest.raises(ValueError):
        function(Person("Samuel"))


def test_decorator_not_raises_if_extracted_property_not_matches_regex():
    @guard.matches_regex(".*el$", property="name")
    def function(person):
        return "name: " + person.name

    function(Person("John"))


# endregion

# region Transformer Tests

def test_decorator_raises_if_transformed_qualifies():
    @guard.none(transformer=lambda v: v.name)
    def function(person):
        return "name: " + person.name

    with pytest.raises(ValueError):
        function(Person(None))


def test_decorator_not_raises_if_transformed_not_qualifies():
    @guard.none(transformer=lambda v: v.name)
    def function(person):
        return "name: " + person.name

    function(Person("John"))


def test_decorator_raises_if_transformed_matches_regex():
    @guard.matches_regex(".*el$", transformer=lambda v: v.name)
    def function(person):
        return "name: " + person.name

    with pytest.raises(ValueError):
        function(Person("Samuel"))


def test_decorator_not_raises_if_transformed_not_matches_regex():
    @guard.matches_regex(".*el$", transformer=lambda v: v.name)
    def function(person):
        return "name: " + person.name

    function(Person("John"))

# endregion
