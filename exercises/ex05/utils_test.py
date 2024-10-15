from exercises.ex05.utils import only_evens, sub, add_at_index

"""Defining unit tests for lists"""

__author__ = "730738053"


def test_only_evens_edge_case() -> None:
    """If only odds are provided, an empty string is returned."""
    assert only_evens([7, 9]) == []


def test_only_evens_use_case_1() -> None:
    """If only evens are provided, an exact copy is returned."""
    assert only_evens([2, 4]) == [2, 4]


def test_only_evens_use_case_2() -> None:
    """If a mix of evens and odds are provided, only the even numbers are returned."""
    assert only_evens([4, 5, 6]) == [4, 6]


def test_sub_edge_case() -> None:
    """If the list is not in the range, an empty list is returned."""
    list = [1, 2, 3, 4]
    assert sub(list, 9, 12) == []


def test_sub_use_case_1() -> None:
    """If part of the list is in the range, that part is returned."""
    list = [10, 11, 12, 13, 14, 15, 16]
    assert sub(list, 4, 6) == [14, 15]


def test_sub_use_case_2() -> None:
    """If the entire list is in the range, a copy of the list is returned."""
    list = [45, 47, 49]
    assert sub(list, 0, 3) == [45, 47, 49]


def test_add_at_index_edge_case() -> None:
    """Adds to an empty list"""
    list = []
    add_at_index(list, 10, 0)
    assert list == [10]


def test_add_at_index_use_case_1() -> None:
    """Adds an element to the middle of the list"""
    list = [25, 26, 28, 29]
    add_at_index(list, 27, 2)
    assert list == [25, 26, 27, 28, 29]


def test_add_at_index_use_case_2() -> None:
    """Adds an element to the beginning of the list."""
    list = [10, 20, 30, 40]
    add_at_index(list, 0, 0)
    assert list == [0, 10, 20, 30, 40]
