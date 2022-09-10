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
- **not_match_regex**
- **not_numeric**
- **not_alphabetic**
- **not_alphanumeric**

## Create a Custom Guard

custom_guard.py:
```python
from guardian import Guard

dead = Guard(name="dead", predicate=lambda v: not v.alive, description="Don't Perform if dead")
alive = Guard(name="alive", predicate=lambda v: v.alive, description="Don't Perform if alive")
```
main.py:
```python
import custom_guard

@custom_guard.dead
def shoot(enemy):
  ...

@custom_guard.alive
def revive(player):
  ... 
<<<<<<< Updated upstream
```
=======
```
>>>>>>> Stashed changes
