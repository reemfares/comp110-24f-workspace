"""Practicing using linked list data structures."""

from __future__ import annotations

__author__ = "730738053"


class Node:
    """Defines the class Node."""

    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        """Establishes values for Node attributes."""
        self.value = val
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of a linked list."""
        rest: str = "TODO"
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))


def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


print(to_str(one))
print(to_str(courses))


def last(head: Node) -> int:
    """Return the last value of a non-empty list."""
    # Base Case: when head is the "last" node
    print(f"Enter last({head.value})")
    if head.next is None:
        print(f"Return base case: {head.value})")
        return head.value
    else:
        # Recursive case:
        rest: int = last(head.next)
        print(f"Return recur: {head.value} -> {rest}")
        return rest


print(last(one))
print(last(courses))


def recursive_range(start: int, end: int) -> Node | None:
    """Build a list recursively from start to end."""
    if start > end:
        raise ValueError("invalid arguments, start > end")
    if start == end:
        # Base Case!
        return None
    else:
        # Recursive Case
        # 1. Handle the first value in your new list here!
        first: int = start
        # 2. Let the rest of the list be handled recusively!
        rest: Node | None = recursive_range(start + 1, end)
        # 3. Return a new node which is first followed by rest!
        return Node(first, rest)


a_list: Node | None = recursive_range(110, 113)
print(a_list)


def value_at(head: Node | None, index: int) -> int:
    """Returns the data of a Node at a certain index in the list."""
    if head is None:
        # Edge Case: raising an error!
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        # Base Case: the index is zero!
        return head.value
    # Recursive Case!
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Returns the maximum data value in the linked list."""
    if head is None:
        # Edge Case: raising an error!
        raise ValueError("Cannot call max with None")
    if head.next is None:
        # Base Case!
        return head.value
    maximum: int = head.value
    # Create a local variable to hold the current maximum value.
    if maximum < max(head.next):
        # Recursive Case!
        maximum = max(head.next)
    return maximum


def linkify(items: list[int]) -> Node | None:
    """Returns a linked list of Nodes of a list."""
    if items == []:
        # Base Case!
        return None
    else:
        # Recursive Case!
        return Node(items[0], linkify(items[1:]))
        # Insert the first value in the list in the Node and then do
        # that again for the rest of the list.


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns a list of the values of another list scaled by a factor."""
    if head is None:
        # Base Case!
        return None
    else:
        # Recursive Case!
        return Node(head.value * factor, scale(head.next, factor))
        # Multiply the first value by the factor and then run the function until
        # reaching the end of the nodes
