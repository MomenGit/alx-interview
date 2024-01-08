#!/usr/bin/python3
"""Defines canUnlockAll function"""


from sympy import true


def canUnlockAll(boxes: list[list]):
    """
    You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1
    and each box may contain keys to the other boxes.

    Determines if all the boxes can be opened
    boxes[0] is unlocked by default

    Args:
        boxes (list[list[int]]): list of boxes
    Returns:
        Default: False
        True, if all the boxes can be opened
    """
    allUnlocked = False
    if boxes:
        allKeys = set()
        usedKeys = set()
        newKeys = set()
        for key in boxes[0]:
            allKeys.add(key)
            newKeys.add(key)
            usedKeys.add(key)
        loop = true
        while loop:
            for key in newKeys:
                for newKey in boxes[key]:
                    allKeys.add(newKey)
            if len(allKeys) >= len(boxes)-1:
                allUnlocked = True
            newKeys = allKeys.difference(usedKeys)
            usedKeys = allKeys.copy()
            loop = len(newKeys) != 0

    return allUnlocked
