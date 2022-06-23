import doctest


def func(n: int):
    """
    >>> func(3)
    8
    >>> func(30)
    1073741824
    """
    return pow(2, n)


def main():
    print(func(int(input())))


if __name__ == '__main__':
    doctest.testmod()
    main()
