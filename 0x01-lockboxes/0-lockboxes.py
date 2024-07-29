#!/usr/bin/python3
"""Module for solving the lockboxes problem"""


def canUnlockAll(boxes):
    """Determines if all boxes can be unlocked.

    Args:
        boxes (list): List of lists representing boxes and their keys.

    Returns:
        bool: True if all boxes can be unlocked, otherwise False.
    """
    total_boxes = len(boxes)
    keys = [0]
    unlocked = set(keys)

    for key in keys:
        for new_key in boxes[key]:
            if new_key not in unlocked:
                unlocked.add(new_key)
                keys.append(new_key)

    return len(unlocked) == total_boxes
