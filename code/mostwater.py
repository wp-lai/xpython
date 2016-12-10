"""
Task:
    Given n non-negative integers a1, a2, ..., an, where each represents a
    point at coordinate (i, ai). n vertical lines are drawn such that the two
    endpoints of line i is at (i, ai) and (i, 0). Find two lines, which
    together with x-axis forms a container, such that the container contains
    the most water. Note: You may not slant the container.

    In other word, We have to maximize the area that can be formed between the
    vertical lines using the shorter line as length and the distance between
    the lines as the width of the rectangle forming the area.

>>> max_area([1, 1])
1
>>> max_area([3, 8, 5, 2])
6
>>> max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
49
"""


def max_area(heights):
    i, j = 0, len(heights) - 1
    maxarea = 0
    while i < j:
        curarea = (j - i) * min(heights[i], heights[j])
        maxarea = max(maxarea, curarea)
        if heights[i] < heights[j]:
            i += 1
        else:
            j -= 1
    return maxarea


if __name__ == '__main__':
    import doctest
    doctest.testmod()
