"""
Task:
    Given an array nums and a value val, remove all instances of that value
    in-place and return the new length. Do not allocate extra space for
    another array, you must do this by modifying the input array in-place with
    O(1) extra memory. The order of elements can be changed. It doesn't matter
    what you leave beyond the new length.

>>> nums, val = [3, 2, 2, 3], 3
>>> res = remove_element(nums, val)
>>> res, nums[0:res]
(2, [2, 2])
>>> nums, val = [0, 1, 2, 2, 3, 0, 4, 2], 2
>>> res = remove_element(nums, val)
>>> res, nums[0:res]
(5, [0, 1, 3, 0, 4])
"""


def remove_element(nums, val):
    size = len(nums)
    index_pre, index_post = 0, 0
    while index_pre < size:
        while nums[index_pre] == val:
            index_pre += 1
            if index_pre >= size:
                return index_post
        nums[index_post] = nums[index_pre]
        index_pre, index_post = index_pre + 1, index_post + 1
    return index_post


if __name__ == "__main__":
    import doctest
    doctest.testmod()
