import doctest
from typing import List


def func(n: int, mochis: List[int]):
    """
    >>> func(4,[10,8,8,6])
    3
    >>> func(3,[15,15,15])
    1
    >>> func(7,[50,30,50,100,50,80,30])
    4
    """
    mochis.sort()
    return len(list(set(mochis)))


def main():
    n = int(input())
    mochis = []
    for x in range(n):
        mochis.append(int(input()))
    print(func(n, mochis))


if __name__ == '__main__':
    doctest.testmod()
    main()
