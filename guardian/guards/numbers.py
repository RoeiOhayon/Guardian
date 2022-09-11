from guardian.guard import Guard

zero = Guard("Zero", lambda v: v == 0, "Zero Guard")

negative = Guard("Negative", lambda v: v < 0, "Negative Guard")
not_negative = Guard("Negative", lambda v: v >= 0, "Negative Guard")

positive = Guard("Positive", lambda v: v > 0, "Positive Guard")
not_positive = Guard("NotPositive", lambda v: v <= 0, "NotPositive Guard")

in_range = Guard("InRange", lambda v, r: r[0] <= v <= r[1], "InRange Guard")
out_of_range = Guard("OutOfRange", lambda v, r: v >= r[1] or v <= r[0], "NotInRange Guard")
