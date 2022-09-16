from guardian import atomic_guards as guard


def main():
    print(f(2))


@guard.zero()
def f(n):
    return n * 2


if __name__ == "__main__":
    main()
