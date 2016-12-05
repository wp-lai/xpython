"""
Task:
    Given two strings, find the longest common substring.
    Return the length of it.

>>> lcs("abcd", "cbce")
2
>>> lcs("83217", "683147")
4
"""


def lcs(str_a, str_b):
    len_a, len_b = len(str_a), len(str_b)
    # tbl[i][j] means the longest common substring of str_a[:i] and str_b[:j]
    tbl = [[0] * (len_b + 1) for _ in range(len_a + 1)]
    for j in range(1, len_b + 1):
        for i in range(1, len_a + 1):
            if str_a[i - 1] == str_b[j - 1]:
                tbl[i][j] = max(tbl[i - 1][j - 1] + 1,
                                tbl[i - 1][j], tbl[i][j - 1])
            else:
                tbl[i][j] = max(tbl[i - 1][j - 1],
                                tbl[i - 1][j], tbl[i][j - 1])
    return tbl[len_a][len_b]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
