"""
Task:
    Given an integer array nums, return the length of the longest strictly
    increasing subsequence. A subsequence is a sequence that can be derived
    from an array by deleting some or no elements without changing the order
    of the remaining elements. For example, [3,6,2,7] is a subsequence of the
    array [0,3,1,6,2,2,7].

>>> length_of_LIS([10, 9, 2, 5, 3, 7, 101, 18])
4
>>> length_of_LIS([0, 1, 0, 3, 2, 3])
4
>>> length_of_LIS([7, 7, 7, 7, 7, 7, 7])
1
"""
import bisect


def length_of_LIS(nums):
    res = []
    for i in nums:
        if not res:
            res.append(i)
        elif res[-1] < i:
            res.append(i)
        else:
            index = bisect.bisect_left(res, i)
            if res[index] != i:
                res[index] = i

    return len(res)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
