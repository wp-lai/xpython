"""
Task:
    Given a sorted array, remove the duplicates in place such that each element
    appear only once and return the new length. Do not allocate extra space for
    another array, you must do this in place with constant memory.
    For example, Given input array nums = [1,1,2], Your function should return
    length = 2, with the first two elements of nums being 1 and 2 respectively.
    It doesn't matter what you leave beyond the new length.

>>> remove_duplicates([1, 1, 2])
2
>>> remove_duplicates([])
0
>>> remove_duplicates([1, 2, 2, 3])
3
"""


def remove_duplicates(nums):
    if not nums:
        return 0

    i, j = 0, 1
    while j < len(nums):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
        j += 1
    return i + 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
