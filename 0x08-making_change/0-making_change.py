#!/usr/bin/python3
"""
module that  determine the fewest
number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """ function to find fewest number of coins needed to meet total """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    diference = 0
    for c in coins:
        if total <= 0:
            break
        temp = total // c
        diference += temp
        total -= (temp * c)
    if total != 0:
        return -1
    return diference
