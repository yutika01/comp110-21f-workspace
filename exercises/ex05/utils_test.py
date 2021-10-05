"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730480382"


def test_only_evens() -> None: 
    """Test for only_evens using one odd."""
    assert only_evens([10, 15, 20]) == [10, 20]


def test_only_evens_again() -> None: 
    """Test for only_evens using two odds."""
    assert only_evens([1, 2, 3]) == [2]


def test_only_evens_again_two() -> None: 
    """Test for only_evens using no odds."""
    assert only_evens([4, 4, 4]) == [4, 4, 4]


def test_sub() -> None:
    """Test for sub."""
    assert sub([3, 4, 5, 6], 1, 4) == [4, 5, 6]


def test_sub_again() -> None:
    """Test for sub using negative start."""
    assert sub([1, 2, 3, 4], -1, 3) == [1, 2, 3]


def test_sub_again_two() -> None:
    """Test for sub using large end value."""
    assert sub([10, 20, 30, 40], 1, 7) == [20, 30, 40]


def test_concat() -> None:
    """Test for concat."""
    assert concat([1, 2, 3, 4], [5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_concat_again() -> None:
    """Test for concat."""
    assert concat([10, 20], [5, 4]) == [10, 20, 5, 4]


def test_concat_again_two() -> None:
    """Test for concat using empty string."""
    assert concat([], [3, 4, 5]) == [3, 4, 5]