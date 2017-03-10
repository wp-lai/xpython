"""
Task:
    Find the kth largest element in an unsorted array. Note that it is the kth
    largest element in the sorted order, not the kth distinct element.

>>> find_kth_largest([3, 2, 1, 5, 6, 4], 2)
5
"""
from random import randint


def find_kth_largest(nums, k):
    # find a random pivot
    length = len(nums)
    pivot = randint(0, length - 1)
    nums[pivot], nums[0] = nums[0], nums[pivot]

    # reorder so that left part > key, right part < key
    key = nums[0]
    i, j = 1, 1
    while j < length:
        if nums[j] > key:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1
    i -= 1
    nums[i], nums[0] = nums[0], nums[i]

    # divide and conqure
    if i == k - 1:
        return nums[i]
    elif i < k - 1:
        return find_kth_largest(nums[i + 1:], k - 1 - i)
    else:
        return find_kth_largest(nums[:i], k)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
