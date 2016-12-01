"""
Question:
    Given a roman numeral, convert it to an integer.
    Input is guaranteed to be within the range from 1 to 3999.


Symbol Value
I 1 (unus)
V 5 (quinque)
X 10 (decem)
L 50 (quinquaginta)
C 100 (centum)
D 500 (quingenti)
M 1,000 (mille)

>>> roman_to_int("DCXXI")
621
>>> roman_to_int("VI")
6
>>> roman_to_int("LXXVI")
76
>>> roman_to_int("XIII")
13
>>> roman_to_int("MMMCMXCIX")
3999
>>> roman_to_int("")
0
"""


def roman_to_int(s):
    values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50,
              'X': 10, 'V': 5, 'I': 1}
    result = 0
    for i in range(len(s)):
        if i == len(s) - 1:
            result += values[s[i]]
        else:
            if values[s[i]] < values[s[i + 1]]:
                result -= values[s[i]]
            else:
                result += values[s[i]]
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
