import doctest
from typing import List


def func(lr: List[List[int]]):
    """
    >>> func([[10,20],[20,30],[40,50]])
    [[10, 30], [40, 50]]
    >>> func([[10,40],[30,60],[20,50]])
    [[10, 60]]
    >>> func([[10,20]])
    [[10, 20]]
    >>> func([[10,20],[30,40],[50,60]])
    [[10, 20], [30, 40], [50, 60]]
    >>> func([[10,70],[20,40],[40,60]])
    [[10, 70]]
    """
    # 10,20
    # 10,20
    # 20,30
    # 10,30
    # 40,50
    #
    lr.sort()
    loginlr = []
    for i in lr:
        loginlr.append([i[0], 0])
        loginlr.append([i[1], 1])
    loginlr.sort()
    cnt: int = 0
    begin: int = 0
    end: int = 0
    ans = []

    for i in loginlr:
        if i[1] == 0:
            if cnt == 0:
                begin = i[0]
            cnt = cnt+1
        else:
            cnt = cnt-1
            if cnt == 0:
                end = i[0]
        if begin != 0 and end != 0:
            ans.append([begin, end])
            begin = 0
            end = 0
    return ans


def main():
    n = (int(input()))
    lr = []
    for i in range(n):
        lr.append(list(int(x)for x in input().split(' ')))
    for res in func(lr):
        print("%d %d" % (res[0], res[1]))

    return


if __name__ == '__main__':
    doctest.testmod()
    main()
