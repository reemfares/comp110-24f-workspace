"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730738053"


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    count: int = 0
    # On line 24, a local variable counts how many of the  if statements are true.
    # On line 24, I forgot that you can edit local variables.

    if word[0] == letter:
        print(letter + " found at index 0")
        count = count + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    if count > 0:
        print(str(count) + " intances of " + letter + " found in " + word)
        # On line 45, I am printing the number of times the letter shows up in the word.
        # On line 45, I forgot to make the local variable, count, a string.


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
