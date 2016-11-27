"""
Question:
    Reverse digits of an integer.

>>> reverse_int(1234)
4321
>>> reverse_int(-3452)
-2543
"""


def reverse_int(x):
    sign = 1 if x >= 0 else -1
    x = sign * x
    result = 0
    while x:
        result = result * 10 + x % 10
        x = x // 10
    return sign * result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
