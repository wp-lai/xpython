"""
Task:
    Given an array S of n integers, are there elements a, b, c in S such that
    a + b + c = 0? Find all unique triplets in the array which gives the sum of
    zero.

>>> three_sum([-1, 0, 1, 2, -1, -4])
[[-1, -1, 2], [-1, 0, 1]]
"""


def three_sum(nums):
    result = []
    nums = sorted(nums)

    for i in range(len(nums)):
        if i > 0 and nums[i - 1] == nums[i]:
            continue

        # compute two sum
        begin, end, target = i + 1, len(nums) - 1, -nums[i]
        while begin < end:
            # pass duplicate item
            if begin > (i + 1) and nums[begin - 1] == nums[begin]:
                begin += 1
                continue

            if (nums[begin] + nums[end]) > target:
                end -= 1
            elif (nums[begin] + nums[end]) < target:
                begin += 1
            else:
                result.append([nums[i], nums[begin], nums[end]])
                begin += 1
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
