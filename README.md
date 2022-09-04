<h1 align="center">
  <img alt="Guardian Logo" width="185px" src="images/Guardian Logo.png" />
</h1>

# Guardian
Guard Clause Package

## Usage

```python
from guardian import guard


@guard.none
def get_by_username(username, users_repository):
    guard.not_alphabtic(username)
    ...
```

## Supported Guard Clauses

- **none** Raises if None
- **negative** Raises if Negative
- **zero** Raises if zero
- **positive** Raises if positive
- **not_in_range** Raises if not in range
- **regex** Raises if not matching
- **not_numeric** Raises if not numeric
- **not_alphabetic** Raises if not alphabetic
- **not_alphanumeric** Raises if not alphanumeric

## Create a Custom Guard

```python
guard.create("dead", labmda v: not v.alive)

@guard.dead
def shoot(enemy):
  ...
```
