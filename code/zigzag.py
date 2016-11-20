"""
Question:
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given
    number of rows like this:

    P       I       N
    A    L  S    I  G
    Y  A    H  R
    P       I

    And then read line by line: ""PINALSIGYAHRPI. Write the code that will take
    a string and make this conversion given a number of rows:

    string convert(string text, int nRows);
    convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

>>> zigzag_convert("PAYPALISHIRING", 3)
'PAHNAPLSIIGYIR'
>>> zigzag_convert("PAYPALISHIRING", 4)
'PINALSIGYAHRPI'
>>> zigzag_convert("", 1)
''
>>> zigzag_convert("ab", 1)
'ab'
"""


def zigzag_convert(s, rows):
    # corner cases
    if len(s) <= rows or rows == 1:
        return s

    # set up initial state
    row = 0
    inc = 1
    result = ["" for _ in range(rows)]

    # put every char in order
    for char in s:
        result[row] += char  # not efficient, but simple to write
        row += inc
        if row == 0 or row == rows - 1:
            inc *= -1  # reverse increment direction

    return "".join(result)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
