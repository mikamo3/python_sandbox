import doctest


def func(cnt: int, total_yen: int):
    """
    >>> func(9,45000)
    [4, 0, 5]
    >>> func(20,196000)
    [-1, -1, -1]
    >>> func(1000,1234000)
    [26, 0, 974]
    >>> func(2000,20000000)
    [2000, 0, 0]
    """
    for x in range(cnt+1)[::-1]:
        if x*10000 > total_yen:
            continue
        for y in range(cnt-x+1)[::-1]:
            if x*10000+y*5000+(cnt-x-y)*1000 == total_yen:
                return [x, y, cnt-x-y]

    return [-1, -1, -1]


def main():
    cnt, total_yen = (int(x) for x in input().split())
    ans = func(cnt, total_yen)
    print("%d %d %d" % (ans[0], ans[1], ans[2]))


if __name__ == '__main__':
    doctest.testmod()
    main()
