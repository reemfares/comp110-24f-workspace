"""Mutating functions."""

__author__ = 730738053


def manual_append(list: list[int], number: int) -> None:
    list.append(number)


def double(list: list[int]) -> None:
    idx: int = 0
    while len(list) > idx:
        list[idx] *= 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
