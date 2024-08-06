#!/usr/bin/python3
"""Module for calculating minimum operations"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed for n 'H' characters.

    Args:
    n (int): The target number of H characters.

    Returns:
    int: Minimum operations needed, or 0 if impossible.
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while factor <= n:
        # If n is divisible by the current factor
        if n % factor == 0:
            # Add the factor to the total operations (Copy All + Paste)
            operations += factor
            # Divide n by the factor (simulating the Paste operation)
            n = n / factor
            # Decrement factor to check for repeated divisions
            factor -= 1
        # Increment factor to check the next potential divisor
        factor += 1

    return operations
