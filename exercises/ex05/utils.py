"""Implementing list utility funcitons"""

__author__ = "730738053"


def only_evens(input: list[int]) -> list[int]:
    """Create list with the even elements of the original list"""
    new_list: list[int] = []  # Adding to a new list instead of modifying
    for elem in input:
        if elem % 2 == 0:  # Adding elements with remainder of 0 when divided by 2
            new_list.append(elem)
    return new_list


def sub(list: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Creates list of the elements of the original list within a range"""
    new_list: list[int] = []
    while start_idx < 0:  # Starting at beginning of list when start index is negative
        start_idx += 1
    while end_idx > len(list):  # Ending at end of list when end index is beyond length
        end_idx -= 1
    if start_idx > len(list):
        return []
    if end_idx <= 0:
        return []
    # If range starts after list ends or ends before list starts, empty list is returned
    while start_idx < end_idx:
        new_list.append(list[start_idx])  # Adds every element within the range
        start_idx += 1
    return new_list


def add_at_index(list: list[int], add: int, place: int) -> None:
    """Adds an integer at a specific index in the list"""
    list.append(0)  # Creates another index for the elements to shift down a place
    idx: int = len(list) - 1  # Starts at the end so it can iterate backwards
    while idx > place:
        list[idx] = list[idx - 1]  # Replaces the last element with the element before
        idx -= 1
    list[place] = add  # Adds the integer in
    if (place > len(list)) or (place < 0):
        raise IndexError("Index is out of bounds for the input list")
