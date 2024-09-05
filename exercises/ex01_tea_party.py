"""Determine the number of items and amount of money needed for our tea party."""

__author__: str = "730738053"


def main_planner(guests: int) -> None:
    """Calculate the cost of the tea party based on the number of guests."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    # On the line that prints out the cost function, I forgot to equate people to guests which is necessary because the function needs arguments. I reviewed my notes and figured it out.


def tea_bags(people: int) -> int:
    """Calculate the number of tea bags needed based on the number of guests."""
    return people * 2


def treats(people: int) -> int:
    """Calculate the number of treats needed based on the number of guests."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the cost of the tea bags and treats needed based on the number of guests."""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
