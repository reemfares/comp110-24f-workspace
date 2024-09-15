"""Practice with conditionals."""


def less_than_10(num: int) -> None:
    """Tell me if num is < 10."""
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("Have a nice day!")


def should_i_eat(hungry: bool) -> None:
    """Tells me whether or not to eat based on hunger."""
    if hungry:  # conditional/boolean expression
        print("Eat some food silly goose!")  # "then" block
    else:
        print("Do your Comp 110 homework instead.")  # "else" block
    print("I'm proud of you <3")  # either way, be kind to yourself


def check_first_letter(word: str, letter: str) -> None:
    """Tells me if the first charecter of the word is the letter."""
    if word[0] == letter:
        print("match!")
    else:
        print("no match!")
