"""
Task:
    Given an array of size n, find the majority element. The majority element
    is the element that appears more than n/2 times.

    You may assume that the array is non-empty and the majority element always
    exist in the array.

>>> major_elem(['a', 'b', 'a'])
'a'
>>> major_elem(['a', 'a', 'b', 'b', 'b'])
'b'
>>> major_elem([3, 3, 4, 2, 4, 4, 2, 4, 4])
4
"""


# if the major element exists, we can use Boyer-Moore majority vote algorithm
def major_elem(nums):
    res, cnt = 0, 0
    for num in nums:
        if not cnt:
            res = num
            cnt += 1
        else:
            cnt += 1 if res == num else -1
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()
