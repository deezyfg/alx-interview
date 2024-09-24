#!/usr/bin/python3
"""Module for calculating the perimeter of an island in a grid."""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (List[List[int]]): A list of lists of integers where:
            0 represents water
            1 represents land

    Returns:
        int: The perimeter of the island

    The function assumes the island is completely surrounded by water,
    and there is only one island (or nothing).
    """

    # Get the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])

    # Initialize perimeter counter
    perimeter = 0

    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # If it's a land cell
                # Check top edge
                top = (i == 0) or (grid[i-1][j] == 0)
                # Check bottom edge
                bottom = (i == rows-1) or (grid[i+1][j] == 0)
                # Check left edge
                left = (j == 0) or (grid[i][j-1] == 0)
                # Check right edge
                right = (j == cols-1) or (grid[i][j+1] == 0)

                # Add the number of edges that are water
                perimeter += top + bottom + left + right

    return perimeter
