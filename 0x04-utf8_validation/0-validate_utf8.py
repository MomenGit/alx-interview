#!/usr/bin/python3
"""Define validUTF8 method for UTF-8 validation"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    Args:
        data (List[int]): a list of integers, where each integer
            represents 1 byte of data
    """
    # (code point, compare against, number of bytes)
    code_points = [(0, 128, 1), (192, 224, 2), (224, 240, 3), (240, 248, 4)]
    byte_index = 0
    while byte_index < len(data):
        length = 0
        for point, comp, bytes in code_points:
            if data[byte_index] & comp == point:
                length = bytes
                byte_index += 1
                break

        if length == 0:
            return False

        for i in range(length-1):
            if data[byte_index] & 192 != 128:
                return False
            byte_index += 1

        byte_index += 1

    return True
