from guardian import guard


def main():
    good_user("asdfasdf")


@guard.regex(".*")
def good_user(username):
    return username


if __name__ == "__main__":
    main()
