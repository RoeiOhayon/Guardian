from guardian.guard import Guard

in_date_range = Guard("InDateRange", lambda v, rng: rng[0] <= v <= rng[1], "Date cannot be in the specified range")
out_of_date_range = Guard("OutOfDateRange", lambda v, rng: v > rng[1] or v < rng[0],
                          "Date cannot be outside the specified range")

after = Guard("AfterDate", lambda v, d: v > d, "Date must be before specified date")
before = Guard("BeforeDate", lambda v, d: v < d, "Date must be after specified date")
