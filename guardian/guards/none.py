from guardian.guard import Guard

none = Guard("None", lambda v: v is None, "None Guard")
