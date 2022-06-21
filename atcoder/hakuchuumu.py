import doctest


def func(s: str):
    """
    >>> func("erasedream")
    'YES'
    >>> func("dreameraser")
    'YES'
    >>> func("dreamerer")
    'NO'
    """
    while s.find('dream') != -1 or s.find('erase') != -1:
        if s.find('dream') == 0:

            s = s[5:]
            if s.find('erase') == 0:
                continue
            if s.find('er') == 0:
                s = s[2:]
        elif s.find('erase') == 0:
            s = s[5:]
            if s.find('r') == 0:
                s = s[1:]

    return "YES" if s == '' else "NO"


def main():
    print(func(input()))


if __name__ == '__main__':
    doctest.testmod()
    main()
