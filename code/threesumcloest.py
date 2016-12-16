"""
Task:
    Given an array S of n integers, find three integers in S such that the sum
    is closest to a given number, target. Return the sum of the three integers.
    You may assume that each input would have exactly one solution.

>>> three_sum_cloest([-1, 2, 1, -4], target=1)
2
>>> three_sum_cloest([0, 0, 0], 1)
0
"""


def three_sum_cloest(nums, target):
    n = len(nums)
    if n <= 3:
        return sum(nums)

    nums = sorted(nums)
    ans = nums[0] + nums[1] + nums[2]
    for i in range(0, n - 2):
        j, k = i + 1, n - 1
        while j < k:
            cur = nums[i] + nums[j] + nums[k]
            if cur == target:
                return target
            elif cur < target:
                j += 1
            else:
                k -= 1

            if abs(cur - target) < abs(ans - target):
                ans = cur
    return ans


if __name__ == '__main__':
    import doctest
    doctest.testmod()
