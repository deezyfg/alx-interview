#!/usr/bin/python3
"""Pascal's Triangle Implementation"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Args:
    n (int): Number of rows to generate.

    Returns:
    list of lists: Pascal's Triangle representation.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j-1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
