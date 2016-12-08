"""
Task:
    Returns the index of the first occurrence of needle in haystack,
    or -1 if needle is not part of haystack.

>>> find("abcd", "bcd")
1
>>> find("abde", "abc")
-1
>>> find("", "")
0
"""


def find(haystack, needle):
    hsk_size, ndl_size = len(haystack), len(needle)
    for i in range(hsk_size - ndl_size + 1):
        if haystack[i:i + ndl_size] == needle:
            return i
    return -1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
