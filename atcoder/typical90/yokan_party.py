import doctest
from typing import List


def func(n: int, l: int, k: int, a: List[int]):
    """
    >>> func(3,34,1,[8,13,26])
    13
    >>> func(3,100,1,[28,54,81])
    46
    >>> func(20,1000,4,[51,69,102,127,233,295,350,388,417,466,469,523,553,587,720,739,801,855,926,954])
    170
    """
    left = -1
    right = l+1
    while right-left > 1:
        mid: int = left + int((right-left)/2)
        if solve(n, l, k, a, mid) == False:
            right = mid
        else:
            left = mid
    return left


def solve(n: int, l: int, k: int, a: List[int], m: int):
    cnt = 0
    pre = 0
    for i in range(n):
        if a[i]-pre >= m and l-a[i] >= m:
            cnt = cnt+1
            pre = a[i]
    return cnt >= k


def main():
    n, l = (int(x) for x in input().split(" "))
    k = int(input())
    a = list(int(x) for x in input().split(" "))
    print(func(n, l, k, a))


if __name__ == '__main__':
    doctest.testmod()
    main()
