import doctest

def func(ip: str):
    """
    >>> func('000')
    0
    >>> func('101')
    2
    >>> func('111')
    3
    """
    cnt = sum([int(x) for x in list(ip)])
    return cnt


if __name__ == '__main__':
    doctest.testmod()

print(func(input()))
