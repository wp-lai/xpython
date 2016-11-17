"""
Question:
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

>>> for two_sum in [two_sum_1, two_sum_2, two_sum_3]:
...    assert two_sum([3, 2, 4], 6) == [1, 2]
...    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
...    assert two_sum([0, 2, 3, 0], 0) == [0, 3]
"""


# Solution 1: double loop
def two_sum_1(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


# Solution 2: two-pass hash table
def two_sum_2(nums, target):
    map_ = {}
    # build a {element: index} map
    for i, num in enumerate(nums):
        map_[num] = i

    for j, num in enumerate(nums):
        complement = target - num
        if complement in map_ and \
           map_[complement] != j:
            return [j, map_[complement]]

    return None


# Solution 3: one-pass hash table
def two_sum_3(nums, target):
    map_ = {}

    # build map while iter
    for i, num in enumerate(nums):
        complement = target - num
        if complement in map_:
            return [map_[complement], i]
        map_[num] = i

    return None


if __name__ == '__main__':
    import doctest
    doctest.testmod()
