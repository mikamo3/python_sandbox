import doctest
from typing import List


def func(plans: List[List[int]]):
    """
    >>> func([[3,1,2],[6,1,1]])
    'Yes'
    >>> func([[2,1,1],[3,2,1],[5,2,3],[7,3,4]])
    'Yes'
    >>> func([[2,100,100]])
    'No'
    >>> func([[5,1,1],[100,1,1]])
    'No'
    """
    time = 0
    current_x = 0
    current_y = 0
    for x in plans:
        traveling_length = abs(x[1]-current_x)+abs(x[2]-current_y)
        if x[0]-time-traveling_length < 0 or (x[0]-time-traveling_length) % 2 != 0:
            return 'No'
        current_x = x[1]
        current_y = x[2]
        time = x[0]

    return 'Yes'


def main():
    n = int(input())
    plans = []
    for x in range(n):
        plans.append(list(int(y) for y in input().split(" ")))
    print(func(plans))


if __name__ == '__main__':
    doctest.testmod()
    main()
