"""
Task:
    Implement the Rabin-Karp's algorithm for searching the given pattern in the
    given text.

>>> get_occurrences("aba", "abacaba")
[0, 4]
>>> get_occurrences("Test", "testTesttesT")
[4]
>>> get_occurrences("aaaaa", "baaaaaaa")
[1, 2, 3]
"""
import random
PRIME = 1000000007
MULTIPLIER = random.randrange(0, PRIME)


def hash_func(s):
    ans = 0
    for c in reversed(s):
        ans = (ans * MULTIPLIER + ord(c)) % PRIME
    return ans


def precompute_hashes(t, p_s):
    H = [0] * (len(t) - p_s + 1)
    H[-1] = hash_func(t[-p_s:])
    y = 1
    for i in range(p_s):
        y = (y * MULTIPLIER) % PRIME
    for i in reversed(range(0, len(t) - p_s)):
        comp = MULTIPLIER * H[i + 1] + ord(t[i]) - y * ord(t[i + p_s])
        H[i] = comp % PRIME
    return H


def get_occurrences(pattern, text):
    result = []
    p_hash = hash_func(pattern)
    p_s, t_s = len(pattern), len(text)
    H = precompute_hashes(text, p_s)
    for i in range(0, t_s - p_s + 1):
        if p_hash != H[i]:
            continue
        if text[i:i + len(pattern)] == pattern:
            result.append(i)
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
