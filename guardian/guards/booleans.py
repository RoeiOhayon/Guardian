from guardian.guard import Guard

true = Guard("True", lambda v: v, "True Guard")
false = Guard("False", lambda v: not v, "False Guard")
