from guardian.guard import Guard

import re

none = Guard("None", lambda v: v is None, "None Guard")
not_matches_regex = Guard("NotMatchesRegex", lambda v, pattern: not re.match(pattern, v), "NotMatchesRegex Guard")
negative = Guard("Negative", lambda v: v < 0, "Negative Guard")
zero = Guard("Zero", lambda v: v == 0, "Zero Guard")
positive = Guard("Positive", lambda v: v > 0, "Positive Guard")
out_of_range = Guard("OutOfRange", lambda v, wanted_range: v > wanted_range[1] or v < wanted_range[0],
                     "NotInRange Guard")
not_numeric = Guard("NotNumeric", lambda v: not v.isnumeric(), "NotNumeric Guard")
not_alphabetic = Guard("NotAlphabetic", lambda v: not v.isalpha(), "NotAlphabetic Guard")
not_alphanumeric = Guard("NotAlphanumeric", lambda v: not v.isalnum(), "NotAlphanumeric Guard")
