"""Uses of lists."""

__author__ = "730738053"


def all(list: list[int], integer: int) -> bool:
    """Checking if the integer is the same as all the number in the list."""
    idx: int = 0
    while idx < len(list):
        if integer != list[idx]:
            return False  # The function will be exited if found to be false.
        idx += 1  # Iterate through every item in the list.
    return True


def max(input: list[int]) -> int:
    """Finding the maximum in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    largest: int = input[0]  # First item starts as the largest.
    idx: int = 1  # Starts at 1 to compare to the first item.
    while idx < len(input):
        if largest < input[idx]:
            largest = input[idx]
        idx += 1
    return largest


def is_equal(list_a: list[int], list_b: list[int]) -> bool:
    """Checking if the lists have the same number in the same order."""
    idx: int = 0
    while (idx < len(list_a)) and (idx < len(list_b)):  # Exits when both lists end.
        if list_a[idx] != list_b[idx]:
            return False  # The function will be exited if the lists are unequal.
        else:
            idx += 1
    return True


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Combining two lists."""
    idx: int = 0
    while idx < len(list_2):
        list_1.append(list_2[idx])  # Iterate through every item of list_2 and add it.
        idx += 1