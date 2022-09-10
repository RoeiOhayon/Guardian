from guardian import guards as guard


def main():
    print(f(19))


@guard.none
def f(n):
    return n * 2


if __name__ == "__main__":
    main()
