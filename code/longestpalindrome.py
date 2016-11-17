"""
Question:
Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000,
and there exists one unique longest palindromic substring.

>>> longest_pal('abccbaab')
'abccba'
>>> longest_pal('a')
'a'
>>> longest_pal('bb')
'bb'
"""


def longest_pal(s):
    """logest palindromic substring in s"""
    longest = ""
    for i in range(len(s)):
        longest = max(longest, expand(i, s),
                      expand(i, s, offset=True),
                      key=len)
    return longest


def expand(pos, s, offset=False):
    """find a palindrome by expanding around the center

    >>> expand(1, 'abc')
    'b'
    >>> expand(1, 'aaa')
    'aaa'
    >>> expand(0, 'bb', True)
    'bb'
    """
    if offset:  # shift right pos by 1
        right = pos + 1
        left = pos
    else:
        left = right = pos
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
