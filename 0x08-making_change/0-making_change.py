#!/usr/bin/python3
"""Module for making change with the fewest coins."""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given
    amount `total` when given a pile of coins of different values.

    Args:
        coins (list): A list of coin denominations available.
        total (int): The total amount for which change is needed.

    Returns:
        int: The fewest number of coins required to make the total.
             Returns 0 if the total is 0 or less.
             Returns -1 if the total cannot be met with the available coins.
    """
    if total <= 0:
        return 0

    current_sum = 0  # Tracks the current sum of the change made
    coin_count = 0   # Tracks the number of coins used

    # Sort coins in descending order
    coins = sorted(coins, reverse=True)

    for coin in coins:
        coin_quantity = (total - current_sum) // coin
        current_sum += coin_quantity * coin
        coin_count += coin_quantity

        if current_sum == total:
            return coin_count

    return -1
