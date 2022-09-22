from guardian import guard


def main():
    print(f(""))


@guard.empty()
@guard.whitespace()
def f(n):
    return n * 2


if __name__ == "__main__":
    main()
