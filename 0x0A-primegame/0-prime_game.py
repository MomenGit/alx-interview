#!/usr/bin/python3
""""""


def isWinner(x, nums):
    """"""
    wins = []

    for round in range(x):
        benWins = True
        n = nums[round]
        prime = [True for i in range(n+1)]
        p = 2

        while (p <= n):
            if (prime[p] == True):
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
