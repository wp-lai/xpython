"""
Task:
    Convert date from day of the month to day of the year.

>>> month_day(1988, 60)
(2, 29)
"""


def month_day(year, day):
    daytab = [[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
              [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]
    leap = 1 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 0

    i = 1
    while (day > daytab[leap][i]):
        day -= daytab[leap][i]
        i += 1
    return (i, day)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
