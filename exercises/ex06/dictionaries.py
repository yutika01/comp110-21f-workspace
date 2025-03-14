"""Practice with dictionaries."""

__author__ = "730480382"

# Define your functions below


def invert(input: dict[str, str]) -> dict[str, str]:
    """Switch keys and values in new dictionary."""
    final: dict[str, str]
    final = {}
    for key in input:
        if input[key] in final:
            raise KeyError("KeyError")
        else:
            final[input[key]] = key
    return final


def favorite_color(names: dict[str, str]) -> str:
    """Return most popular color in dictionary."""
    popular: str = ""
    maxcount: int = 0
    count_dict: dict[str, int] = {}
    for item in names:
        if names[item] in count_dict:
            count_dict[names[item]] += 1
        else: 
            count_dict[names[item]] = 1
    for item in count_dict:
        if count_dict[item] > maxcount:
            maxcount = count_dict[item]
            popular = item
    return popular


def count(input: list[str]) -> dict[str, int]:
    """Return count of each color in list."""
    final_count: dict[str, int]
    final_count = {}
    for item in input:
        if item in final_count:
            final_count[item] += 1
        else: 
            final_count[item] = 1
    return final_count