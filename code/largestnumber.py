"""
Question:
    Given a list of non negative integers, arrange them such that they form the
    largest number. For example, given [3, 30, 34, 5, 9], the largest formed
    number is 9534330.

>>> largest_number([3, 30, 34, 5, 9])
'9534330'
>>> largest_number([0, 0])
'0'
"""
from functools import cmp_to_key  # compatible with python3


def largest_number(numbers):
    numbers = sorted((str(i) for i in numbers),
                     key=cmp_to_key(my_cmp_func),
                     reverse=True)
    result = ''.join(numbers).lstrip('0')  # remove leading '0'
    return result or '0'  # incase empty str


def my_cmp_func(x, y):
    """

    >>> my_cmp_func('2', '21')
    1
    """
    if x + y >= y + x:
        return 1
    else:
        return -1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
