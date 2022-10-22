"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    frequencies = dict.fromkeys(items, 0)
    for i in frequencies:
        frequencies[i] = items.count(frequencies[i])
    return frequencies
