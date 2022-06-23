import doctest
from functools import reduce


def func(n: int, a: int, b: int):
    """
    >>> func(20,2,5)
    84
    >>> func(10,1,2)
    13
    >>> func(100,4,16)
    4554
    """
    sum = reduce(lambda x, y: x+sum_target_value(y, a, b), list(range(n+1)))

    return sum


def sum_target_value(n: int, a: int, b: int):
    """
    >>> sum_target_value(24,2,6)
    24
    >>> sum_target_value(24,2,5)
    0
    """
    tsum = reduce(lambda a, b: a+b, list(map(int, str(n))))
    return n if tsum >= a and tsum <= b else 0


def main():
    n, a, b = (int(x) for x in input().split(' '))
    print(func(n, a, b))


if __name__ == "__main__":
    doctest.testmod()
    main()
