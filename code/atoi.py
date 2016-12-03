"""
Task:
    Implement atoi to convert a string to an integer.

Requirements for atoi:
    The function first discards as many whitespace characters as necessary
    until the first non-whitespace character is found. Then, starting from this
    character, takes an optional initial plus or minus sign followed by as many
    numerical digits as possible, and interprets them as a numerical value.

    The string can contain additional characters after those that form the
    integral number, which are ignored and have no effect on the behavior of
    this function.

    If the first sequence of non-whitespace characters in str is not a valid
    integral number, or if no such sequence exists because either str is empty
    or it contains only whitespace characters, no conversion is performed.

    If no valid conversion could be performed, a zero value is returned.
    If the correct value is out of the range of representable values,
    INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

>>> atoi("86765")
86765
>>> atoi("  +0  123")
0
>>> atoi("")
0
>>> atoi("-")
0
>>> atoi("2147483648")
2147483647
>>> atoi("-2147483649")
-2147483648
"""
INT_MIN = -2147483648
INT_MAX = 2147483647


def atoi(s):
    value = ""
    for i, char in enumerate(s.lstrip()):
        if (i == 0 and char in '+-') or char.isdigit():
            value += char
        else:
            break

    # check '', '+', '-' case
    if value in '+-':
        return 0

    value = int(value)
    # make sure value is within [INT_MIN, INT_MAX]
    return min(max(value, INT_MIN), INT_MAX)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
