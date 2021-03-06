"""
Task:
    You are given two integer arrays nums1 and nums2 both of unique elements,
    where nums1 is a subset of nums2. Find all the next greater numbers for
    nums1's elements in the corresponding places of nums2. The Next Greater
    Number of a number x in nums1 is the first greater number to its right in
    nums2. If it does not exist, return -1 for this number.

>>> next_greater_element([4, 1, 2], [1, 3, 4, 2])
[-1, 3, -1]
>>> next_greater_element([2, 4], [1, 2, 3, 4])
[3, -1]
"""


def next_greater_element(nums1, nums2):
    res_map = {}
    stack = []
    for num in nums2:
        while stack and stack[-1] < num:
            res_map[stack.pop()] = num
        stack.append(num)
    for num in stack:
        res_map[num] = -1
    return [res_map[x] for x in nums1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
