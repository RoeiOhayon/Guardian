<h1 align="center">
  <img alt="Guardian Logo" width="185px" src="images/Guardian Logo.png" />
</h1>

[![Python](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10-2596be)](https://python.org)
[![PyPI](https://img.shields.io/badge/PyPI-v1.1.0-33CA58)](https://pypi.org/project/guardian-python/)
[![PyPI](https://img.shields.io/badge/email-roeiohayon1652%40gmail.com-darkviolet)](https://gmail.com)
[![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=https://github.com/RoeiOhayon/Guardian)

# Guardian
A [Guard Clause](https://en.wikipedia.org/wiki/Guard_(computer_science)) is a validation of information used to avoid errors during execution, and enables to ["fail fast"](https://en.wikipedia.org/wiki/Fail-fast).<br/>
This package provides:
- Function decorator guard clauses (All function arguments will be checked)
- General use case guard clauses
- Ability to create custom guard clauses

## Install
```
pip install guardian-python
```

## Usage

```python

from guardian import guard


@guard.none()
def buy_item(username: str, users_repository: UsersRepository, products_repository: ProductsRepository):
    guard.not_alphabetic(username)
    ...
```

## Supported Guard Clauses

- **numbers:** zero, not_negative, not_positive, in_range, out_of_range
- **strings:** matches_regex, not_matches_regex, whitespace, uppercase, lowercase, not_numeric, not_alphabetic, not_alphanumeric, empty_or_whitespace
- **dates:** in_date_range, out_of_date_range, before, after
- **general:** none, contains, equals, empty (list, str, tuple...) 

## Create a Custom Guard

custom_guard.py:
```python
from guardian import Guard

dead = Guard(name="dead", predicate=lambda v: v.HP + v.armor <= 0, description="Don't Perform if dead")
alive = Guard(name="alive", predicate=lambda v: v.HP + v.armor > 0, description="Don't Perform if alive")
```
main.py:
```python
import custom_guard

@custom_guard.dead()
def shoot(enemy: Enemy):
  ...

@custom_guard.alive()
def revive(player: Player):
  ... 
```

## Additional Parameters
- **property:** extracts property from objects
- **key:** get value at key
- **transformer:** function to extract wanted data to guard against
```python
@guard.none(property="name")
def login(user: User):
  # if user.name is None an exception will be thrown

@guard.none(key="name")
def login(user: dict):
  # if user["name"] is None an exception will be thrown

@guard.none(transformer=lambda v: v.name)
def login(user: User):
  # if user.name is None an exception will be thrown
```

## More Code Examples:
```python
guard.matches_regex(".*el$")
def greet_user(username: str):
  # username = "Daniel" will throw an exception
  # username = "John" won't throw an exception
  ...

# Alternatively you can use:
def greet_user(username: str):
  guard.matches_regex(username, ".*el$")
  ...

@guard.out_of_range([0, 255])
def rgb_to_hsv(r: int, g: int, b: int) -> Tuple[int, int, int]:
  ...
```

Feel free to give a ⭐ if you enjoy using this project 😊
