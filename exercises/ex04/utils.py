"""List utility functions."""

__author__ = "730480382"


# TODO: Implement your functions here.

def all(items: list[int], num: int) -> bool:
    """Determine whether all elements are the same as the number."""
    i: int = 0
    if len(items) == 0:
        return False
    while i < len(items):
        if list(i) != num:
            return False
        else:
            i += 1
    return True

def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Determine whether the two lists are equal."""
    i: int = 0
    if len(list1) == len(list2):
        while i < len(list1) and i < len(list2): 
            if list1[i] == list2[i]:
                return True
            else:
                i += 1
    return False

def max(inputlist: list[int]) -> int:
    """Determine maximum value in an input list."""
    if len(inputlist) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    j: int = i + 1
    maxvalue: int = inputlist[0]
    while i < len(inputlist):
        j = i + 1
        while j < len(inputlist):
            if inputlist[i] < inputlist[j]:
                maxvalue = inputlist[j]
            j += 1
        i += 1
    return maxvalue