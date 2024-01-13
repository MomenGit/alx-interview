#!/usr/bin/python3
"""Defines canUnlockAll function"""


def traverse(currentBox, boxes, unlockedBoxes):
    """Recursively traverse unlocked boxes"""
    for key in currentBox:
        if len(unlockedBoxes) == len(boxes):
            break
        if 0 <= key < len(boxes) and not unlockedBoxes.__contains__(key):
            unlockedBoxes.add(key)
            traverse(boxes[key], boxes, unlockedBoxes)


def canUnlockAll(boxes):
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
    allUnlocked = True
    if boxes:
        unlockedBoxes = set()
        unlockedBoxes.add(0)
        traverse(boxes[0], boxes, unlockedBoxes)
        allUnlocked = len(unlockedBoxes) == len(boxes)

    return allUnlocked
