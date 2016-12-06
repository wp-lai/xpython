"""
Task:
    Write a function to find the longest common prefix string amongst an array
    of strings.

>>> lcp(["leets", "leetcode", "leet", "leeds"])
'lee'
>>> lcp([])
''
"""


def lcp(strs):
    if not strs:
        return ''

    prefix = strs[0]
    result = ""

    for index in range(len(prefix)):
        for s in strs[1:]:
            if index >= len(s):
                return result
            if s[index] != prefix[index]:
                return result
        result += prefix[index]
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
