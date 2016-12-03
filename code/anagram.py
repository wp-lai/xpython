"""
Task:
    Anagram Detection. One string is an anagram of another if the second is
    simply a rearrangement of the first. Write a boolean function that will
    take two strings and return whether they are anagrams.

>>> is_anagram('heart', 'earth')
True
>>> is_anagram('python', 'typhon')
True
>>> is_anagram('pleap', 'apple')
True
>>> is_anagram('anagram', 'hangram')
False
"""


# Solution 1: sort and compare
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)


# Solution 2: count and compare
# Variation 1
def is_anagram(str1, str2):
    map1 = {}
    for char in str1:
        map1[char] = map1.get(char, 0) + 1

    map2 = {}
    for char in str2:
        map2[char] = map2.get(char, 0) + 1

    return map1 == map2


# Variation 2
def is_anagram(str1, str2):
    from collections import Counter
    return Counter(str1) == Counter(str2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
