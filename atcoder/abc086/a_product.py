import doctest


def func(a: int, b: int):
    """
    >>> func(3,4)
    'Even'
    >>> func(1,21)
    'Odd'
    """

    return 'Even' if a*b % 2 == 0 else 'Odd'


def main():
    a, b = (int(x) for x in input().split())
    print(func(a, b))


if __name__ == '__main__':
    doctest.testmod()
    main()
