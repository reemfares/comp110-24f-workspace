"""Determining the maximum value of the list"""

__author__ = "730738053"


def find_and_remove_max(input: list[int]) -> int:
    if input == []:
        return -1
    max: int = input[0]
    for elem in input:
        if elem > max:
            max = elem
    idx: int = 0
    while idx < len(input):
        if input[idx] == max:
            input.pop(idx)
        else:
            idx += 1
    return max
