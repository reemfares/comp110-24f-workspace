"""File to define Fish class."""

__author__ = "730738053"


class Fish:
    """Defining the class Fish."""

    age: int

    def __init__(self) -> None:
        """Establishes values for Fish attributes."""
        self.age = 0
        return None

    def one_day(self) -> None:
        """Adds a day to the age everyday."""
        self.age += 1  # Adds one to age.
        return None
