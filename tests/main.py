from guardian import atomic_guards as guard


def main():
    guard.none(3)


def f(n):
    return n * 2


if __name__ == "__main__":
    main()
