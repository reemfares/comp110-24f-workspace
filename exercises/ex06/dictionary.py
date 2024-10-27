"""Practicing with dictionary fucntion"""

__author__ = "730738053"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Switch the key and value in the dictionary"""
    inverted_dictionary: dict[str, str] = {}  # Creates an empty dictionary
    for elem in dictionary:  # Interates through keys in the dictionary
        if dictionary[elem] in inverted_dictionary:  # Error is raised if keys repeat
            raise KeyError(
                f"{dictionary[elem]} is already present in invert_dictionary."
            )
        inverted_dictionary[dictionary[elem]] = elem  # Switches the key and value
    return inverted_dictionary


def favorite_color(fav_list: dict[str, str]) -> str:
    """Determine which color is the most students favorite"""
    color_count: dict[str, int] = {}  # Creates an empty dictionary
    for elem in fav_list:  # Iterates through keys in the dictionary
        if fav_list[elem] not in color_count:
            color_count[fav_list[elem]] = 0  # Adds a color to the dictionary
        color_count[fav_list[elem]] += 1  # Adds to how many people favor that color
    best_color: str = ""
    highest_vote: int = 0
    for colors in color_count:
        if (
            color_count[colors] > highest_vote
        ):  # If color favored more than previous fav
            highest_vote = color_count[colors]  # New most amount favoring one color
            best_color = colors  # New favorite color
    return best_color


def count(values: list[str]) -> dict[str, int]:
    """Attribute the number of times a value is repeated with the value"""
    counting_values: dict[str, int] = {}  # Creates an empty dictionary
    for elem in values:  # Iterates through keys in the list
        if elem in counting_values:  # If value already present adds to times repeated
            counting_values[elem] += 1
        else:  # Creates new key with the value
            counting_values[elem] = 1
    return counting_values


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Group words that start with the same letter together"""
    first_letter: dict[str, list[str]] = {}  # Creates an empty dictionary
    for elem in words:
        if elem[0].lower() not in first_letter:
            first_letter[elem[0].lower()] = [
                elem
            ]  # Creates a new key in the dictionary
        else:
            first_letter[elem[0].lower()].append(elem)  # Adds to an already present key
    return first_letter


def update_attendance(attendance: dict[str, list[str]], days: str, name: str) -> None:
    """Add a name to attendance on a day of the week"""
    if days not in attendance:
        attendance[days] = []  # Creates a day with attendence if it's not present
    if name not in attendance[days]:
        attendance[days].append(name)  # Adds the person to attendance on the day
