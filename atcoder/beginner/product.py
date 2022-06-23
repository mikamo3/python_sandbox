import doctest


def func(i: str):
    """
    >>> func('2 2')
    'Even'
    >>> func('2 3')
    'Even'
    >>> func('1 3')
    'Odd'
    """
    a, b = (int(x) for x in i.split())
    if a % 2 != 0 and b % 2 != 0:
        return 'Odd'
    return 'Even'


if __name__ == '__main__':
    doctest.testmod()

print(func(input()))
