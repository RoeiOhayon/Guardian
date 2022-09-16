from guardian.guard import Guard

none = Guard("None", lambda v: v is None, "Value must not be None")
