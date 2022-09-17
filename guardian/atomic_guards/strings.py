from guardian.guard import Guard
import re

matches_regex = Guard("MatchesRegex", lambda v, pattern: bool(re.match(pattern, v)),
                      "String must not match specified pattern")
not_matches_regex = Guard("NotMatchesRegex", lambda v, pattern: not re.match(pattern, v),
                          "String match specified pattern")

numeric = Guard("Numeric", lambda v: v.isnumeric(), "String must not be numeric")
not_numeric = Guard("NotNumeric", lambda v: not v.isnumeric(), "String must be numeric")

alphabetic = Guard("Alphabetic", lambda v: v.isalpha(), "String must not be alphabetic")
not_alphabetic = Guard("NotAlphabetic", lambda v: not v.isalpha(), "String must be alphabetic")

alphanumeric = Guard("Alphanumeric", lambda v: v.isalnum(), "String must not be alphanumeric")
not_alphanumeric = Guard("NotAlphanumeric", lambda v: not v.isalnum(), "String must be alphanumeric")

# is_not_whitespace, is not empty, lowercase, uppercase, guard.not_in-not_equals

# list is_not_empty, contains ?,
