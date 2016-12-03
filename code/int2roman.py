"""
Task:
    Convert integer to Roman numerals, assume input <= 3999

Symbol Value
I 1 (unus)
V 5 (quinque)
X 10 (decem)
L 50 (quinquaginta)
C 100 (centum)
D 500 (quingenti)
M 1,000 (mille)

>>> roman_num(6)
'VI'
>>> roman_num(76)
'LXXVI'
>>> roman_num(13)
'XIII'
>>> roman_num(44)
'XLIV'
>>> roman_num(3999)
'MMMCMXCIX'
"""


def roman_num(num):
    value_symbols = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                     (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
                     (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    res = ""
    for value, symbol in value_symbols:
        digit, num = divmod(num, value)
        res += digit * symbol
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()
