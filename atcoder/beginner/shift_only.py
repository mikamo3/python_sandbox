import doctest


def func(inp1: str, inp2: str):
    """
    >>> func('4','5 6 8 10')
    0
    >>> func('6','382253568 723152896 37802240 379425024 404894720 471526144')
    8
    """
    min: int = pow(2, 31)
    tarr = [int(x) for x in inp2.split()]
    for x in tarr:
        for n in range(0, 31):
            if is_nth_bit_set(x, n) is True:
                min = n if min > n else min
                break
    return min


def is_nth_bit_set(num: int, n: int):
    """
    >>> is_nth_bit_set(2,0)
    False
    >>> is_nth_bit_set(2,1)
    True
    >>> is_nth_bit_set(16,4)
    True
    >>> is_nth_bit_set(17,0)
    True
    """

    if num & (1 << n):
        return True
    return False


if __name__ == '__main__':
    doctest.testmod()
print(func(input(), input()))
