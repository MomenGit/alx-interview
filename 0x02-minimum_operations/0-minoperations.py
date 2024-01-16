#!/usr/bin/python3
"""In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste.
Given a number n
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters in the file.
    """
    file = 1
    ops = 0
    copy = 0
    while file < n:
        if n % file == 0:
            copy = file  # Copies the file
            ops += 1

        file = file + copy  # Pastes to the file
        ops += 1

    return ops
