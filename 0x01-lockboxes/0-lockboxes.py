#!/usr/bin/python3
"""n number of boxes. each box may contain keys to the other boxes"""


def canUnlockAll(boxes):
    """check if we can unlock all boxes"""
    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < num_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                stack.append(key)

    return all(unlocked_boxes)
