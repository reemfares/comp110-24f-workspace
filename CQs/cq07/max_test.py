from CQs.cq07.find_max import find_and_remove_max

"""Defining unit tests"""

__author__ = "730738053"


def test_find_and_remove_max_use_case_1() -> None:
    """Returns expected value"""
    assert find_and_remove_max([12, 24, 27, 18]) == 27


def test_find_and_remove_max_use_case_2() -> None:
    """Mutates input in expected way"""
    input = [1, 2, 3, 4, 4]
    find_and_remove_max(input)
    assert input == [1, 2, 3]


def test_find_and_remove_max_edge_case() -> None:
    """Returns correct value for empty list"""
    input = []
    assert find_and_remove_max(input) == -1
