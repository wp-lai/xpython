"""
Task:
    Given an integer array nums, find the sum of the elements between indices
    i and j (i ≤ j), inclusive.

Constraints:
    + 0 <= nums.length <= 104
    + -105 <= nums[i] <= 105
    + 0 <= i <= j < nums.length
    + At most 104 calls will be made to sumRange.

>>> num_array = [-2, 0, 3, -5, 2, -1]
>>> query = NumArray(num_array)
>>> query.sum_range(0, 2)
1
>>> query.sum_range(2, 5)
-1
>>> query.sum_range(0, 5)
-3
"""


class NumArray:

    def __init__(self, nums):
        self.__presum = [0]
        for i in range(1, len(nums) + 1):
            lastsum = self.__presum[-1]
            self.__presum.append(nums[i - 1] + lastsum)

    def sum_range(self, i, j):
        return self.__presum[j + 1] - self.__presum[i]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
