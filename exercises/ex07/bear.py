"""File to define Bear class."""

__author__ = "730738053"


class Bear:
    """Defining the class Bear."""

    age: int
    hunger_score: int

    def __init__(self) -> None:
        """Establishes values for Fish attributes."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self) -> None:
        """Adds a day to the age everyday."""
        self.age += 1  # Adds one to age.
        self.hunger_score -= 1  # Subtracts one from hunger score.
        return None

    def eat(self, num_fish: int) -> None:
        """Increases the hunger score."""
        self.hunger_score += num_fish  # Adds the number of fish to the hunger score.
        return None
