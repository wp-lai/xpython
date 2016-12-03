"""
Task:
    Compute Modular exponentiation, which is a type of exponentiation performed
    over a modulus.
    See: https://www.wikiwand.com/en/Modular_exponentiation

>>> mod_pow(4, 13, 497)
445
>>> mod_pow(3, 1000, 7)
4
>>> mod_pow(7, 107, 9) == pow(7, 107, 9)
True
"""


# Solution 1
def mod_pow(base, exponent, modulus):
    result = 1
    for _ in range(1, exponent + 1):
        result = (result * base) % modulus
    return result


# Solution 2
def mod_pow(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent = exponent // 2
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
