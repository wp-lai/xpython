"""
Task:
    Given a string, find the length of the
    longest substring without repeating characters.


>>> len_longest_substring("abcabcbb")
3
>>> len_longest_substring("")
0
>>> len_longest_substring("bbbbb")
1
>>> len_longest_substring("pwwkew")
3
>>> len_longest_substring("a")
1
"""


def len_longest_substring(s):
    start = 0
    # dict to keep the index of seen characters
    index_map = {}
    max_len = 0

    for index, char in enumerate(s):
        if char in index_map and index_map[char] >= start:
            start = index_map[char] + 1
        index_map[char] = index
        max_len = max(max_len, index - start + 1)

    return max_len


if __name__ == '__main__':
    import doctest
    doctest.testmod()
