"""Sets the number of species and prints the number overtime."""

from exercises.ex07.river import River

__author__ = "730738053"


my_river: River = River(num_fish=10, num_bears=2)  # Sets the number of each species.

my_river.view_river()  # Shows how many of each species overtime.
