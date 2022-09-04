<p align="center">
  <img alt="Guardian Logo" width="185px" src="images/Guardian Logo.png" />
</p>

# Guardian
Guard Clause Package

## Usage

```
from guardian import guard


@guard.none  # If any argument is None an Error will be raised
def get_user_by_username(username, users_repository):
    guard.is_alphabetic(username)  # If username is not alphabetic an Error will be raised
```
