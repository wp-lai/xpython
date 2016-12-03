"""
Task:
    Find greatest common divisor

>>> gcd(54, 24)
6
>>> gcd(299792458, 6447287)
511
"""


# Using Euclid's algorithm
# Variation 1
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# Variation 2: recursive version
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
