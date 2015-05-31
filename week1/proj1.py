"""
Project 1: merge a line (part of 2048 game)
"""


def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    new_line = slide(line)
    for pos in range(0, len(line)):
        if pos != len(new_line) - 1 and new_line[pos] == new_line[pos + 1]:
            new_line[pos] *= 2
            new_line[pos + 1] = 0
            new_line = slide(new_line)
    return new_line


def slide(line):
    """
    Slide all numbers to the left
    """
    new_line = list(line)
    for pos, number in enumerate(new_line):
        if number == 0:
            for after_pos in range(pos + 1, len(new_line)):
                if new_line[after_pos] != 0:
                    new_line[pos] = new_line[after_pos]
                    new_line[after_pos] = 0
                    break
    return new_line
