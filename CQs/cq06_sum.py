"""Summing the elements of a list using different loops"""

__author__ = 730738053


def w_sum(vals: list[float]) -> float:
    """Summing the elements of a list using a while loop"""
    idx: int = 0
    sum: float = 0.0  # If the list is empty, it will return 0.0.
    while idx < len(vals):  # Goes until all of the elements are done
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Summing the elements of a list using a for...in... loop"""
    sum: float = 0.0
    for elem in vals:  # Iterates through the elements
        sum += elem  # Adds each element to the initial 0.0
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Summing the elements of a list using the for... in range(...) loop"""
    sum: float = 0.0
    for idx in range(0, len(vals)):  # Iterates through the indices (not elements)
        sum += vals[idx]  # Adds each element to the inital 0.0
    return sum
