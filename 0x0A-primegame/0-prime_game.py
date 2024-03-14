#!/usr/bin/python3
"""
Maria and Ben are playing a game.
Given a set of consecutive integers starting from 1 up to and including n,
they take turns choosing a prime number from the set and
removing that number and its multiples from the set.
The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally,
determine who the winner of each game is.
"""


def isWinner(x, nums):
    """ Determines the prime game winner
    Args:
        x (int): the number of rounds
        nums (List[int]): is an array of n
    """
    wins = []

    for round in range(x):
        benWins = True
        n = nums[round]
        prime = [True for i in range(n+1)]
        p = 2

        while (p <= n):
            if (prime[p] is True):
                for i in range(p*p, n+1, p):
                    prime[i] = False
                benWins = not benWins
            p += 1

        wins.append('Maria' if not benWins else 'Ben')

    mariaWins = wins.count('Maria')
    benWins = wins.count('Ben')

    if mariaWins > benWins:
        return 'Maria'
    elif mariaWins == benWins:
        return None
    else:
        return 'Ben'
