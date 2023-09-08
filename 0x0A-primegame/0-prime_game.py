#!/usr/bin/python3
"""
Prime Game
"""


def prime_nums(n):
    """
    Generatesa list of prime numbers between 1
    and a given upper bound n.
    """
    prime_num = []
    filter = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filter[prime]):
            prime_num.append(prime)
            for index in range(prime, n + 1, prime):
                filter[index] = False
    return prime_num


def isWinner(x, nums):
    """
    This function determines the winner of the Prime
    Game for a given number of rounds x and a list of
    upper limits nums for each round.
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        primenumbers = prime_nums(nums[i])
        if len(primenumbers) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
