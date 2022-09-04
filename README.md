<h1 align="center">
  <img alt="Guardian Logo" width="185px" src="images/Guardian Logo.png" />
</h1>

# Guardian
Guard Clause Package

## Usage

```python
from guardian import guard


@guard.none  # If any argument is None an Error will be raised
def get_user_by_username(username, users_repository):
    guard.is_alphabetic(username)  # If username is not alphabetic an Error will be raised
```

## Supported Guard Clauses

- **none**
- **negative**
- **zero**
- **positive**
- **regex**
- **not_numeric**
- **not_alphabetic**
- **not_alphanumeric**

## Create a Custom Guard

```python
guard.create("alive", labmda v: v.alive)

@guard.alive
def shoot(enemy):
  ...
```
