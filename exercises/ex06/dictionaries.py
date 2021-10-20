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
    num: int = -1
    maxcount = 0
    count_dict: dict[str, int] = {}
    for key in names:
        for second in names:
            if key == second:
                num += 1
        count_dict[key] = num
        num = -1
    for key in count_dict:
        if count_dict[key] > maxcount:
            maxcount = count_dict[key]
            popular = key
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