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

- **none**
- **negative**
- **zero**
- **positive**
- **not_in_range**
- **regex**
- **not_numeric**
- **not_alphabetic**
- **not_alphanumeric**

## Create a Custom Guard

```python
guard.create("dead", labmda v: not v.alive)

@guard.dead
def shoot(enemy):
  ...
```
