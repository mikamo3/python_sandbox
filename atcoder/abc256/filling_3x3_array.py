
import doctest


def func(h1: int, h2: int, h3: int, w1: int, w2: int, w3: int):
    """
    >>> func(3,4,6,3,3,7)
    1
    >>> func(5,13,10,6,13,9)
    120
    >>> func(20,25,30,22,29,24)
    30613
    """
    cnt = 0
    h1arr = ps(h1)
    h2arr = ps(h2)
    h3arr = ps(h3)
    for x in h1arr:
        for x2 in h2arr:
            for x3 in h3arr:
                if x[0]+x2[0]+x3[0] == w1 and x[1]+x2[1]+x3[1] == w2 and x[2]+x2[2]+x3[2] == w3:
                    cnt = cnt+1
    return cnt


def ps(h: int):
    arr = []
    for x in range(1, h):
        for y in range(1, h-x):
            arr.append([x, y, h-x-y])
    return arr


def main():
    h1, h2, h3, w1, w2, w3 = (int(x) for x in input().split(' '))
    print(func(h1, h2, h3, w1, w2, w3))


if __name__ == '__main__':
    doctest.testmod()
    main()
