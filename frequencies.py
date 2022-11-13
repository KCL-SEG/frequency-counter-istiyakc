"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    frequencies = {}
    list = [str(item) for item in items]
    frequencies = dict.fromkeys(items,0)

    for i in list:

        if list[i] in frequencies:

            frequencies[i] += 1
        else:
            frequencies[i] = 1


    return frequencies
