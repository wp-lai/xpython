"""
Task:
    You are given a 2D array of integers envelopes where
    envelopes[i] = [wi, hi] represents the width and the height of an envelope.
    One envelope can fit into another if and only if both the width and height
    of one envelope is greater than the width and height of the other envelope.
    Return the maximum number of envelopes can you Russian doll (i.e., put one
    inside the other). Note: You cannot rotate an envelope.

>>> envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
>>> max_envelopes(envelopes)
3
>>> envelopes = [[1, 1], [1, 1], [1, 1]]
>>> max_envelopes(envelopes)
1
>>> envelopes = [[4,5],[4,6],[6,7],[2,3],[1,1]]
>>> max_envelopes(envelopes)
4
"""


# def longest_increasing_subsequence(arr):
#     print(f"arr {arr}")
#     res = [1 for _ in arr]
#     for i in range(1, len(arr)):
#         for j in range(0, i):
#             if arr[i] > arr[j] and res[i] <= res[j]:
#                 res[i] = res[j] + 1
#     print(f"res {res}")
#     return max(res)


def max_envelopes(envelopes):
    res = [1 for _ in envelopes]
    sorted_by_width = sorted(envelopes, key=lambda x: x[0])

    for i in range(1, len(envelopes)):
        for j in range(0, i):
            if sorted_by_width[i][0] > sorted_by_width[j][0] and \
                sorted_by_width[i][1] > sorted_by_width[j][1] and \
                    res[i] <= res[j]:
                res[i] = res[j] + 1

    return max(res)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
