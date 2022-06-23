import doctest
from typing import List


def func(num_of_card: int, suits: List[int]):
    """
    >>> func(2,[3,1])
    2
    >>> func(3,[2,7,4])
    5
    >>> func(4,[20,18,2,18])
    18
    >>> func(5,[20,18,18,3,2])
    19
    """
    list.sort(suits, reverse=True)
    sum_a = suits.pop(0)
    sum_b = suits.pop(0)

    for i, x in enumerate(suits):
        if i % 2 == 0:
            sum_a=sum_a+x
        else:
            sum_b=sum_b+x
    return sum_a-sum_b 


def main():
    print(func(int(input()), list((int(x) for x in input().split(" ")))))


if __name__ == '__main__':
    doctest.testmod()
    main()
