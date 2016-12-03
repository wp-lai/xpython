"""
Task:
    Given a set of n segments {[a0,b0],[a1,b1]....[an-1,bn-1]} with integer
    coordinates on a line, find the minimum number 'm' of points such that
    each segment contains at least one point .That is,  find a set of
    integers X of the minimum size such that for any segment [ai,bi] there
    is a point x belongs X such that ai <= x <= bi

>>> minimum_points([(1, 3), (2, 5), (3, 6)])
1
>>> minimum_points([(4, 7), (1, 3), (2, 5), (5, 6)])
2
"""


def minimum_points(segments):
    points = []
    segs = sorted(segments, key=lambda x: x[1])
    for seg in segs:
        # check whether this segements is covered by points
        if points and any(seg[0] <= p <= seg[1] for p in points):
            continue

        # safe first move to add smallest end point or largest start point
        points.append(seg[1])
    return len(points)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
