#!/usr/bin/python3
"""Defines makeChange function"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0

    table = [total+1 for i in range(total+1)]
    table[0] = 0

    for i in range(1, total+1):

        for coin in coins:
            if coin > i:
                continue
            diff = i-coin
            change = 0
            if table[diff] != 0 or diff == 0:
                change = table[diff]+1
            if change < table[i]:
                table[i] = change

        if table[i] == total+1:
            table[i] = 0

    if table[-1] == 0:
        return -1

    return table[-1]
