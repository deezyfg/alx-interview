#!/usr/bin/python3
"""
Module containing the solution for the Prime Game problem.
"""


def sieve_of_eratosthenes(n):
    """
    Generate a list of prime numbers up to the given limit (n)
    using the Sieve of Eratosthenes.

    This implementation is adapted from a solution on StackOverflow:
    https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188

    Args:
        limit (int): The upper limit for generating primes.

    Returns:
        list: A list of prime numbers from 2 up to the given limit.
    """
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = [False] * len(sieve[i*i::i])
    return [i for i in range(2, n + 1) if sieve[i]]


def play_single_round(n):
    """
    Play a single round of the Prime Game.

    Args:
        n (int): The upper limit for the current round.

    Returns:
        str: 'Maria' if Maria wins, 'Ben' if Ben wins.
    """
    primes = sieve_of_eratosthenes(n)
    # Maria wins if the number of primes is odd; Ben wins if it's even
    return 'Maria' if len(primes) % 2 == 1 else 'Ben'


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game over multiple rounds.

    Args:
        x (int): Number of rounds to be played.
        nums (list): A list of upper limits for each round.

    Returns:
        str or None: 'Maria' if Maria wins, 'Ben' if Ben wins,
                     or None if it's a tie or invalid input.
    """
    if not isinstance(x, int) or x < 1 or not nums or x != len(nums):
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_single_round(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
