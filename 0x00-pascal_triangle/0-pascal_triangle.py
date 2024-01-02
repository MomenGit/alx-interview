#!/usr/bin/python3
"""Defines pascal_triangle function"""


def pascal_triangle(n: int) -> list[list[int]]:
    """
    returns a list of lists of integers
    representing the Pascal's triangle of n
    """
    triangle = []
    if n <= 0:
        return triangle
    triangle.append([1])
    if n >= 2:
        for i in range(1, n):
            row = [1]
            for j in range(len(triangle[-1])-1):
                row.append(triangle[-1][j]+triangle[-1][j+1])
            row.append(1)
            triangle.append(row)

    return triangle
