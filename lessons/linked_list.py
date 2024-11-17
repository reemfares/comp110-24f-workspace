from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        self.value = val
        self.next = next


two: Node = Node(2, None)
one: Node = Node(1, two)


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
