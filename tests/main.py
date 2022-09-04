from guardian import guard


def main():
    guard.not_alphabetic("3")


@guard.not_numeric
def good_user(username):
    return username


if __name__ == "__main__":
    main()
