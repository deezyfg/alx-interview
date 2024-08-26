#!/usr/bin/python3
"""
Module for solving the N-Queens problem.

This module provides functions to solve the N-Queens puzzle,
which involves placing N chess queens on an N×N chessboard
so that no two queens threaten each other.
"""

import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    n_q = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if n_q < 4:
    print('N must be at least 4')
    exit(1)


def solve_nqueens(n):
    """
    Solve the N-Queens problem for a given board size.

    Args:
    n (int): The size of the chessboard and the number of queens to place.

    Returns:
    list: A list of solutions, where each solution is a
          list of queen positions.
          Each position is represented
          as a tuple (row, column).
    """
    if n == 0:
        return [[]]
    inner_solution = solve_nqueens(n - 1)
    return [solution + [(n, i + 1)]
            for i in range(n_q)
            for solution in inner_solution
            if safe_queen((n, i + 1), solution)]


def attack_queen(square, queen):
    """
    Determine if two queens are attacking each other.

    Args:
    square (tuple): The position (row, column) of the first queen.
    queen (tuple): The position (row, column) of the second queen.

    Returns:
    bool: True if the queens are attacking each other, False otherwise.
    """
    (row1, col1) = square
    (row2, col2) = queen
    return (row1 == row2) or (col1 == col2) or\
        abs(row1 - row2) == abs(col1 - col2)


def safe_queen(sqr, queens):
    """
    Check if a queen can be safely placed in a given position.

    Args:
    sqr (tuple): The position (row, column) to check.
    queens (list): List of positions of queens already on the board.

    Returns:
    bool: True if the position is safe, False otherwise.
    """
    for queen in queens:
        if attack_queen(sqr, queen):
            return False
    return True


for answer in reversed(solve_nqueens(n_q)):
    result = []
    for p in [list(p) for p in answer]:
        result.append([i - 1 for i in p])
    print(result)
