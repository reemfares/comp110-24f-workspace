"""File to define River class."""

__author__ = "730738053"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Defining the class River."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int) -> None:
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Removes old animals."""
        new_fish_list: list[Fish] = []
        for elem in self.fish:  # Removes the fish older than 3.
            if elem.age <= 3:
                new_fish_list.append(elem)
        self.fish = new_fish_list
        new_bears_list: list[Bear] = []
        for animal in self.bears:  # Removes the bears older than 5.
            if animal.age <= 5:
                new_bears_list.append(animal)
        self.bears = new_bears_list
        return None

    def remove_fish(self, amount: int) -> None:
        """Removes the specified amout of fish."""
        idx: int = 0
        while idx < amount:
            self.fish.pop(idx)
            idx += 1
        return None

    def bears_eating(self) -> None:
        """Removes the fish that the bears eat."""
        for elem in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
            elem.eat(3)
        return None

    def check_hunger(self) -> None:
        """Removes starved bears."""
        new_bears_list: list[Bear] = []
        for elem in self.bears:
            if elem.hunger_score >= 0:  # Removes bears if hunger score is below 0.
                new_bears_list.append(elem)
        self.bears = new_bears_list
        return None

    def repopulate_fish(self) -> None:
        """Adds newborn fish."""
        newfish = len(self.fish) // 2  # Adds 4 fish for every 2 fish.
        for i in range(4 * newfish):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self) -> None:
        """Adds newborn bears."""
        newbear = len(self.bears) // 2  # Adds a bear for every 2 bears.
        for i in range(newbear):
            self.bears.append(Bear())
        return None

    def view_river(self) -> None:
        """States how many animals there are on a given day."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self) -> None:
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
        return None

    def one_river_week(self):
        """Goes through the days in a week."""
        for i in range(7):  # Calls the day method 7 times.
            self.one_river_day()
        return None
