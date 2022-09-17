from guardian import atomic_guards as guard


def main():
    print(guard.in_range(235, [234]))


@guard.in_range([1, 10])
def f(n):
    return n * 2


if __name__ == "__main__":
    main()
