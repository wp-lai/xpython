"""
Task:
    Determine whether an integer is a palindrome.

>>> is_pal_number(0)
True
>>> is_pal_number(-1)  # don't consider negative integer palindrome
False
>>> is_pal_number(123321)
True
>>> is_pal_number(123)
False
"""


def is_pal_number(x):
    if x < 0:
        return False

    rev = 0
    temp = x
    while temp:
        rev = rev * 10 + temp % 10
        temp = temp // 10
    return rev == x


if __name__ == '__main__':
    import doctest
    doctest.testmod()
