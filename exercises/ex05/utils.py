"""List utility functions part 2."""

__author__ = "730480382"

# Define your functions below


def only_evens(input: list[int]) -> list[int]:
    """Return only evens in list."""
    i: int = 0
    for item in input:
        if item % 2 != 0:
            input.pop(i)
        i += 1
    return input


def sub(input: list[int], start: int, end: int) -> list[int]:
    """Return a subset of the original list."""
    subset: list[int] = []
    if start < 0:
        start = 0
    if end > len(input):
        end = len(input)
    if end <= 0:
        return subset
    i: int = start
    while i < end:
        subset.append(input[i])
        i += 1
    return subset


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Concatenate the two original lists into a new list."""
    joined: list[int] = []
    for item in list1:
        joined.append(item)
    for item in list2:
        joined.append(item)
    return joined