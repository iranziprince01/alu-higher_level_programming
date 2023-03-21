#!/usr/bin/python3
"""Module 14-pascal_triangle.
Returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """Returns the pascal triangle of n.
    Args:
        - n: size of the triangle (rows)
    Returns: a list of list of integers
    """

    if n <= 0:
        return []

    t = [[0 for x in range(m + 1)] for m in range(n)]
    t[0] = [1]

    for m in range(1, n):
        t[m][0] = 1
        for p in range(1, m + 1):
            if p < len(t[m - 1]):
                t[m][p] = t[m - 1][p - 1] + t[m - 1][p]
            else:
                t[m][p] = t[m - 1][0]
    return t
