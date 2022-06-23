import doctest
from functools import reduce


def func(s: str):
    """
    >>> func('101')
    2
    >>> func('000')
    0
    """
    return reduce(lambda a, b: int(a+1) if b == 1 else int(a), (int(x) for x in s))


def main():
    print(func(input()))


if __name__ == '__main__':
    doctest.testmod()
    main()
