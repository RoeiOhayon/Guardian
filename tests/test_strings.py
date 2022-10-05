from guardian import guard
import pytest


# region MatchesRegex Guard Tests

def test_raises_if_matches_regex():
    with pytest.raises(ValueError):
        guard.matches_regex("hello", "hello")


def test_not_raises_if_not_matches_regex():
    guard.matches_regex("goodbye", "hello")


def test_decorator_raises_if_one_arg_matches_regex():
    @guard.matches_regex("hello")
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function("a", "b", "hello")


def test_decorator_not_raises_if_no_arg_matches_regex():
    @guard.matches_regex("hello")
    def function(a, b, c):
        return a or b or c

    function("good", "bye", "sir")


# endregion

# region NotMatchesRegex Guard Tests

def test_raises_if_not_matches_regex():
    with pytest.raises(ValueError):
        guard.not_matches_regex("goodbye", "hello")


def test_not_raises_if_not_not_matches_regex():
    guard.not_matches_regex("hello hello", "hello")


def test_decorator_raises_if_one_arg_not_matches_regex():
    @guard.not_matches_regex("hello")
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function("hello", "hello", "goodbye")


def test_decorator_not_raises_if_no_arg_not_matches_regex():
    @guard.not_matches_regex(".*there$")
    def function(a, b, c):
        return a or b or c

    function("hi there", "hello there", "it is nice there")


# endregion

# region Numeric Guard Tests

def test_raises_if_numeric():
    with pytest.raises(ValueError):
        guard.numeric("1234")


def test_not_raises_if_not_numeric():
    guard.numeric("hello")


def test_decorator_raises_if_one_arg_is_numeric():
    @guard.numeric()
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function("hello", "hello", "1234")


def test_decorator_not_raises_if_no_arg_is_numeric():
    @guard.numeric()
    def function(a, b, c):
        return a or b or c

    function("a", "bc", "def")


# endregion

# region NotNumeric Guard Tests

def test_raises_if_not_numeric():
    with pytest.raises(ValueError):
        guard.not_numeric("hello")


def test_not_raises_if_not_not_numeric():
    guard.not_numeric("1234")


def test_decorator_raises_if_one_arg_is_not_numeric():
    @guard.not_numeric()
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function("1234", "5678", "hello")


def test_decorator_not_raises_if_no_arg_is_not_numeric():
    @guard.not_numeric()
    def function(a, b, c):
        return a or b or c

    function("1", "23", "456")


# endregion

# region Alphabetic Guard Tests

def test_raises_if_alphabetic():
    with pytest.raises(ValueError):
        guard.alphabetic("hello")


def test_not_raises_if_not_alphabetic():
    guard.alphabetic("123abc")


def test_decorator_raises_if_one_arg_is_alphabetic():
    @guard.alphabetic()
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function("1234abc", "5678def", "hello")


def test_decorator_not_raises_if_no_arg_is_alphabetic():
    @guard.alphabetic()
    def function(a, b, c):
        return a or b or c

    function("1a", "23bc", "456def")


# endregion

# region NotAlphabetic Guard Tests

def test_raises_if_not_alphabetic():
    with pytest.raises(ValueError):
        guard.not_alphabetic("1234hello")


def test_not_raises_if_not_not_alphabetic():
    guard.not_alphabetic("hello")


def test_decorator_raises_if_one_arg_is_not_alphabetic():
    @guard.not_alphabetic()
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function("hello", "there", "123hello")


def test_decorator_not_raises_if_no_arg_is_not_alphabetic():
    @guard.not_alphabetic()
    def function(a, b, c):
        return a or b or c

    function("a", "bc", "def")


# endregion

# region Alphanumeric Guard Tests

def test_raises_if_alphanumeric():
    with pytest.raises(ValueError):
        guard.alphanumeric("1234hello")


def test_not_raises_if_not_alphanumeric():
    guard.alphanumeric("hello there")
    guard.alphanumeric("1234 !")


def test_decorator_raises_if_one_arg_is_alphanumeric():
    @guard.alphanumeric()
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function("hello!", "1234? @", "1234hello")


def test_decorator_not_raises_if_no_arg_is_alphanumeric():
    @guard.alphanumeric()
    def function(a, b, c):
        return a or b or c

    function("a!", "123?", "*!?@")


# endregion

# region NotAlphanumeric Guard Tests

def test_raises_if_not_alphanumeric():
    with pytest.raises(ValueError):
        guard.not_alphanumeric("hello 1234")


def test_not_raises_if_not_not_alphanumeric():
    guard.not_alphanumeric("hello")
    guard.not_alphanumeric("1234")
    guard.not_alphanumeric("hello1234")


def test_decorator_raises_if_one_arg_is_not_alphanumeric():
    @guard.not_alphanumeric()
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function("hello", "1234", "1234hello @*?!")


def test_decorator_not_raises_if_no_arg_is_not_alphanumeric():
    @guard.not_alphanumeric()
    def function(a, b, c):
        return a or b or c

    function("abc", "123", "abc123")


# endregion

# region Whitespace Guard Tests

def test_raises_if_whitespace():
    with pytest.raises(ValueError):
        guard.whitespace("  ")


def test_not_raises_if_not_whitespace():
    guard.whitespace("  hello")
    guard.whitespace("hello there")
    guard.whitespace("hello   ")


def test_decorator_raises_if_one_arg_is_whitespace():
    @guard.whitespace()
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function("hello", "1234 and &", "    ")


def test_decorator_not_raises_if_no_arg_is_whitespace():
    @guard.whitespace()
    def function(a, b, c):
        return a or b or c

    function("hello ", "there, ", " bye!")


# endregion

# region Lowercase Guard Tests

def test_raises_if_lowercase():
    with pytest.raises(ValueError):
        guard.lowercase("hello")


def test_not_raises_if_not_lowercase():
    guard.lowercase("HELLO ")
    guard.lowercase("1234")
    guard.lowercase("There")


def test_decorator_raises_if_one_arg_is_lowercase():
    @guard.lowercase()
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function("HELLO", "There", "goodbye")


def test_decorator_not_raises_if_no_arg_is_lowercase():
    @guard.lowercase()
    def function(a, b, c):
        return a or b or c

    function("THERE", "Hello", " ")


# endregion

# region Uppercase Guard Tests

def test_raises_if_uppercase():
    with pytest.raises(ValueError):
        guard.uppercase("HELLO THERE")


def test_not_raises_if_not_uppercase():
    guard.uppercase("hello")
    guard.uppercase("There ")
    guard.uppercase("1234")


def test_decorator_raises_if_one_arg_is_uppercase():
    @guard.uppercase()
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function("hello", "There", "GOODBYE")


def test_decorator_not_raises_if_no_arg_is_uppercase():
    @guard.uppercase()
    def function(a, b, c):
        return a or b or c

    function("There", "hello", " ")


# endregion

# region EmptyOrWhitespace Guard Tests

def test_raises_if_empty_or_whitespace():
    with pytest.raises(ValueError):
        guard.empty_or_whitespace("   ")
    with pytest.raises(ValueError):
        guard.empty_or_whitespace("")


def test_not_raises_if_not_empty_or_whitespace():
    guard.empty_or_whitespace(" hello")
    guard.empty_or_whitespace("There ")
    guard.empty_or_whitespace("!*@")


def test_decorator_raises_if_one_arg_is_empty_or_whitespace():
    @guard.empty_or_whitespace()
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function("hello", " There", " ")
    with pytest.raises(ValueError):
        function("hello", " There", "")


def test_decorator_not_raises_if_no_arg_is_empty_or_whitespace():
    @guard.empty_or_whitespace()
    def function(a, b, c):
        return a or b or c

    function(" There", "hello ", "123")


# endregion

# region NotURL Guard Tests


def test_raises_if_not_url():
    with pytest.raises(ValueError):
        guard.not_url("https:/hello.com")


def test_not_raises_if_not_not_url():
    guard.not_url("http://localhost:/files")


def test_decorator_raises_if_one_arg_is_not_url():
    @guard.not_url()
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function("http://www.hello.com", "https://hi.com", "hello there.com")


def test_decorator_not_raises_if_no_arg_is_not_not_url():
    @guard.not_url()
    def function(a, b, c):
        return a or b or c

    function("http://www.hello.com", "https://hi.com", "https://hello.there.www")


# endregion

# region NotEmail Guard Tests


def test_raises_if_not_email():
    with pytest.raises(ValueError):
        guard.not_email(" guardian-python@gmail.com")


def test_not_raises_if_not_not_email():
    guard.not_email("guardianpython@gmail.com")


def test_decorator_raises_if_one_arg_is_not_email():
    @guard.not_email()
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function("guardianpython@gmail.com", "hi@outlook.com", "hello there.com")


def test_decorator_not_raises_if_no_arg_is_not_not_email():
    @guard.not_email()
    def function(a, b, c):
        return a or b or c

    function("guardianpython@gmail.com", "a@g.com", "python@isgreat.ongmail.com")


# endregion

# region NotIPv4 Guard Tests


def test_raises_if_not_ipv4():
    with pytest.raises(ValueError):
        guard.not_ipv4("10.20.2.266")


def test_not_raises_if_not_not_ipv4():
    guard.not_ipv4("255.22.10.36")


def test_decorator_raises_if_one_arg_is_not_ipv4():
    @guard.not_ipv4()
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function("10.20.10.55", "255.210.36.47", "10.0.0.266")


def test_decorator_not_raises_if_no_arg_is_not_not_ipv4():
    @guard.not_ipv4()
    def function(a, b, c):
        return a or b or c

    function("10.20.10.55", "255.210.36.47", "11.22.33.44")


# endregion

# region NotBase64 Guard Tests


def test_raises_if_not_base64():
    with pytest.raises(ValueError):
        guard.not_base64("1234*")


def test_not_raises_if_not_not_base64():
    guard.not_base64("aGVsbG8gdGhlcmUgYnJvdGhlcnMgYW5kIHNpc3RlcnM=")


def test_decorator_raises_if_one_arg_is_not_base64():
    @guard.not_base64()
    def function(a, b, c):
        return a or b or c

    with pytest.raises(ValueError):
        function("aGVsbG8gdGhlcmUgYnJvdGhlcnMgYW5kIHNpc3RlcnM=", "dmVyeSBjb29sIHJlZ2V4", "I'm not base64!")


def test_decorator_not_raises_if_no_arg_is_not_not_base64():
    @guard.not_base64()
    def function(a, b, c):
        return a or b or c

    function("dmVyeSBjb29sIHJlZ2V4", "aGVsbG8gdGhlcmUgYnJvdGhlcnMgYW5kIHNpc3RlcnM=", "aGFoYSEhISE=")

# endregion
