"""
Question:
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays.
The overall run time complexity should be O(log(m+n)).

>>> find_median([1, 3], [2])
2
>>> find_median([1, 2], [3, 4])
2.5
>>> find_median([6], [7])
6.5
>>> find_median([1], [1])
1.0
"""


# This problem can convert to finding the kth smallest number
# of two sorted arrays
def find_median(nums1, nums2):
    n = len(nums1) + len(nums2)
    if n % 2:
        return find_kth(nums1, nums2, n // 2 + 1)
    else:
        left = find_kth(nums1, nums2, n // 2)
        right = find_kth(nums1, nums2, n // 2 + 1)
        return (left + right) / 2.0


def find_kth(nums1, nums2, k):
    """find kth number of two sorted arrays

    >>> find_kth([1, 3], [2], 2)
    2
    >>> find_kth([2], [1, 3], 1)
    1
    >>> find_kth([1, 3], [2], 3)
    3
    >>> find_kth([1], [2], 1)
    1
    >>> find_kth([1], [2], 2)
    2
    """
    # assume len(nums1) <= len(nums2)
    if len(nums2) < len(nums1):
        nums1, nums2 = nums2, nums1

    # if nums1 is empty
    if not nums1:
        return nums2[k - 1]

    if k == 1:
        return min(nums1[0], nums2[0])

    # divide and conquer
    if len(nums1) < k // 2:
        return find_kth(nums1, nums2[k - k // 2:], k // 2)
    elif nums1[k // 2 - 1] == nums2[k - k // 2 - 1]:
        return nums1[k // 2 - 1]
    elif nums1[k // 2 - 1] < nums2[k - k // 2 - 1]:
        return find_kth(nums1[k // 2:], nums2[:k - k // 2], k - k // 2)
    else:
        return find_kth(nums1[:k // 2], nums2[k - k // 2:], k // 2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
