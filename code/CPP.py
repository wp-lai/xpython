"""
Question:
    Given n points on a plane, find the smallest distance between a pair of
    two (different) points.

>>> points = [(4, 4), (-2, -2), (-3, -4), (-1, 3), (2, 3), (-4, 0), (1, 1),
...              (-1, -1), (3, -1), (-4, 2), (-2, 4)]
>>> "{:.3f}".format(comp_min_dist(points))
'1.414'
"""
from math import sqrt
INF = 1e15


def dist(t1, t2):
    return sqrt((t1[0] - t2[0]) ** 2 + (t1[1] - t2[1]) ** 2)


def brute_force_comp_min_dist(points):
    n = len(points)
    min_dist = INF
    for i in range(n):
        for j in range(i + 1, n):
            min_dist = min(min_dist, dist(points[i], points[j]))
    return min_dist


def comp_min_dist_wrap(points_x, points_y):
    n = len(points_x)
    if n <= 3:
        return brute_force_comp_min_dist(points_x)
    l_x = points_x[:n // 2]
    r_x = points_x[n // 2:]
    m = (l_x[-1][0] + r_x[0][0]) / 2  # divide by a vertical line
    l_y, r_y = [], []
    for point in points_y:
        if point[0] < m:
            l_y.append(point)
        else:
            r_y.append(point)
    l_dist = comp_min_dist_wrap(l_x, l_y)
    r_dist = comp_min_dist_wrap(r_x, r_y)
    min_dist = min(l_dist, r_dist)
    within_range_points = [p for p in points_y if abs(p[0] - m) <= min_dist]
    n_within = len(within_range_points)
    if n_within <= 1:
        return min_dist
    else:
        for i in range(n_within - 1):
            for j in range(i + 1, n_within):
                if (within_range_points[j][1] - within_range_points[i][1] >
                        min_dist):
                    break
                cur_dist = dist(within_range_points[i], within_range_points[j])
                min_dist = min(min_dist, cur_dist)
    return min_dist


def comp_min_dist(points):
    points_x = sorted(points, key=lambda x: x[0])
    points_y = sorted(points, key=lambda x: x[1])
    return comp_min_dist_wrap(points_x, points_y)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
