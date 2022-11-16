"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    frequencies = {}
    for i in items:
        if (str(i) not in frequencies.keys()):
            frequencies[str(i)] = 1
        else:
            current = frequencies[str(i)] + 1

            frequencies[str(i)] = current

    return frequencies
