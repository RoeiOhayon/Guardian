from guardian.guard import Guard

in_date_range = Guard("InDateRange", lambda v, r: r[0] <= v <= r[1], "Date cannot be in the specified range")
out_of_date_range = Guard("OutOfDateRange", lambda v, r: v > r[1] or v < r[0],
                          "Date cannot be outside the specified range")

after = Guard("InDateRange", lambda v, d: v > d, "Date must be before specified date")
before = Guard("InDateRange", lambda v, d: v < d, "Date must be after specified date")
