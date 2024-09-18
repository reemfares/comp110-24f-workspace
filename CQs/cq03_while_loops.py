"""Practicing while loops in a challange question."""

__author__ = 730738053


def num_instances(phrase: str, search_char: str) -> int:
    """Counting the number of times a charecter shows up in a phrase."""
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if search_char == phrase[index]:
            count += 1
        index += 1
    return count
