import doctest


def func(input_1: str, input_2: str, input_3: str):
    """
    >>> func('12','34 56','test')
    '102 test'
    """
    s: int = int(input_1) + int(input_2.split(' ')
                                [0])+int(input_2.split(' ')[1])
    return str(s) + ' ' + input_3


if __name__ == "main":
    doctest.testmod()

print(func(input(), input(), input()))
