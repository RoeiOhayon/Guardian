from guardian.guard import Guard
import re

not_matches_regex = Guard("NotMatchesRegex", lambda v, pattern: not re.match(pattern, v), "NotMatchesRegex Guard")
not_numeric = Guard("NotNumeric", lambda v: not v.isnumeric(), "NotNumeric Guard")
not_alphabetic = Guard("NotAlphabetic", lambda v: not v.isalpha(), "NotAlphabetic Guard")
not_alphanumeric = Guard("NotAlphanumeric", lambda v: not v.isalnum(), "NotAlphanumeric Guard")
