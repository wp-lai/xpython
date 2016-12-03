"""
Task:
    You are given a set of points on a line and a set of segments on a line.
    The goal is to compute, for each point, the number of segments that contain
    this point.

Hints:
    Given three points x1=5, x2=8, x3=3
    two segments [a1, b1] = [4, 10], [a2, b2] = [2, 6].
    We can transform the data into following list:
    (5,p),(8,p),(3,p),(4,l),(10,r),(2,l),(6,r)
    Then sort it:
    (2,l),(3,p),(4,l),(5,p),(6,r),(8,p),(10,r)
    The result is easier to compute in this form.

>>> count_segments([0, 7], [5, 10], [1, 6, 11])
[1, 0, 0]
>>> count_segments([-10], [10], [-100, 100, 0])
[0, 0, 1]
>>> count_segments([0, -3, 7], [5, 2, 10], [1, 6])
[2, 0]
"""


def count_segments(starts, ends, points):
    data = []
    for sp in starts:
        data.append((sp, 'l'))  # 'l' indicate start points
    for ep in ends:
        data.append((ep, 'r'))  # 'r' indicate end points
    for index, point in enumerate(points):
        data.append((point, 'p', index))  # keep index info

    data.sort(key=lambda x: x[0])
    result = [0] * len(points)
    cnt = 0
    for elem in data:
        if elem[1] == 'l':
            cnt += 1
        elif elem[1] == 'r':
            cnt -= 1
        elif elem[1] == 'p':
            result[elem[2]] = cnt
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
