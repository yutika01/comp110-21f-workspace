"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count
import pytest

__author__ = "730480382"


def test_invert() -> None:
    """Check if function inverts key and value."""
    assert invert({'a': 'a', 'b': 'c', 'd': 'e', 'f': 'g'}) == {'a': 'a', 'c': 'b', 'e': 'd', 'g': 'f'}


def test_invert_again() -> None:
    """Check if it gives error."""
    with pytest.raises(KeyError):
        my_dictionary = {'b': 'c', 'd': 'e', 'f': 'e'}
        invert(my_dictionary)


def test_invert_two() -> None:
    """Check if function inverts key and value."""
    assert invert({'apple': 'pear', 'shoe': 'leg', 'hammock': 'seat'}) == {'pear': 'apple', 'leg': 'shoe', 'seat': 'hammock'}


def test_favorite_color() -> None:
    """Check if it returns favorite color."""
    assert favorite_color({'abby': 'pink', 'claire': 'blue', 'rose': 'pink'}) == "pink"


def test_favorite_color_again() -> None:
    """Check if it returns the first of a tie."""
    assert favorite_color({'abby': 'pink', 'claire': 'blue', 'megan': 'pink', 'jorge': 'blue'}) == "pink"


def test_favorite_color_two() -> None:
    """Check if it returns favorite color."""
    assert favorite_color({'johnson': 'blue', 'david': 'grey', 'megan': 'yellow', 'claire': 'green'}) == 'blue'


def test_count() -> None:
    """Check if it returns counts for each value."""
    assert count(['apple', 'pear', 'umbrella', 'apple', 'confetti', 'pear', 'apple']) == {'apple': 3, 'pear': 2, 'umbrella': 1, 'confetti': 1}


def test_count_again() -> None:
    """Check if it returns counts for each value."""
    assert count(['hello', 'how', 'are', 'you']) == {'hello': 1, 'how': 1, 'are': 1, 'you': 1}


def test_count_two() -> None:
    """Check if it returns counts for each value."""
    assert count(['who', 'who', 'who', 'how', 'How']) == {'who': 3, 'how': 1, 'How': 1}