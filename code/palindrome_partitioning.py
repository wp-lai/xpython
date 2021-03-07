"""
Task:
    Given a string s, partition s such that every substring of the partition
    is a palindrome. Return all possible palindrome partitioning of s. A
    palindrome string is a string that reads the same backward as forward.

>>> partition("aab")
[['a', 'a', 'b'], ['aa', 'b']]
>>> partition("a")
[['a']]
"""


def partition(s):
    n = len(s)
    edge = [[True] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            edge[i][j] = (s[i] == s[j]) and edge[i + 1][j - 1]

    res = []
    path = []

    def dfs(i):
        if i == n:
            res.append(path[:])
            return
        for j in range(i, n):
            if edge[i][j]:
                path.append(s[i:j+1])
                dfs(j + 1)
                path.pop()

    dfs(0)
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()
