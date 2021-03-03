"""
Task:
    Given a non negative integer number num. For every numbers i in the range
    0 ≤ i ≤ num calculate the number of 1's in their binary representation and
    return them as an array.

>>> count_bits(2)
[0, 1, 1]
>>> count_bits(5)
[0, 1, 1, 2, 1, 2]
"""


def count_bits(num):
    if num == 0:
        return [0]
    elif num == 1:
        return [0, 1]
    result = [0] * (num + 1)
    result[1] = 1
    for i in range(2, num + 1):
        result[i] = result[i // 2] + result[i % 2]
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
