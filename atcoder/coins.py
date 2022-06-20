import doctest


def func(coin_500: int, coin_100: int, coin_50: int, target_price: int):
    """
    >>> func(2,2,2,100)
    2
    >>> func(5,1,0,150)
    0
    >>> func(30,40,50,6000)
    213
    """
    cnt = 0
    for c_500 in range(coin_500+1):
        for c_100 in range(coin_100+1):
            for c_50 in range(coin_50+1):
                if c_500*500+c_100*100+c_50*50 == target_price:
                    cnt = cnt+1
    return cnt


def main():
    print(func(int(input()), int(input()), int(input()), int(input())))


if __name__ == ('__main__'):
    doctest.testmod()
    main()
