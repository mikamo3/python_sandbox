import doctest
from typing import List


def func(n: int, a: List[int]):
    """
    >>> func(4,[1,1,3,2])
    3
    >>> func(10,[2,2,4,1,1,1,4,2,2,1])
    8
    """
    ans = 0
    for x in range(n):
        sum = 0
        for y in range(x, n):
            sum = sum+a[y]
            if sum >= 4:
                ans = ans+1
                break
    return ans


def main():
    n = int(input())
    a = list(int(x) for x in input().split())
    print(func(n, a))


if __name__ == '__main__':
    doctest.testmod()
    main()
