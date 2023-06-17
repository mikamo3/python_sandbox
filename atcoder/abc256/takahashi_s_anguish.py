import doctest
from typing import List


def func(x: List[int], c: List[int]):
    """
    >>> func([2,3,2],[1,10,100])
    10
    >>> func([7,3,5,5,8,4,1,2],[36,49,73,38,30,85,27,45])
    57
    """
    ang = []
    for idx, x in enumerate(x):
        ang.append([x * c[idx], idx])


if __name__ == '__main__':
    doctest.testmod()
