#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    t = [[1]]
    while len(t) != n:
        s = t[-1]
        v = [1]
        for m in range(len(s) - 1):
            v.append(s[m] + s[m + 1])
        v.append(1)
        t.append(v)
    return t
