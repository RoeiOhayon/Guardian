from guardian.guard import Guard

zero = Guard("Zero", lambda v: v == 0, "Number cannot be 0")

negative = Guard("Negative", lambda v: v < 0, "Number cannot be negative")
not_negative = Guard("Negative", lambda v: v >= 0, "Number must not be negative")

positive = Guard("Positive", lambda v: v > 0, "Number cannot be positive")
not_positive = Guard("NotPositive", lambda v: v <= 0, "Number must not be positive")

in_range = Guard("InRange", lambda v, r: r[0] <= v <= r[1], "number cannot be in the specified range")
out_of_range = Guard("OutOfRange", lambda v, r: v > r[1] or v < r[0], "number cannot be outside the specified range")
