"""Coding the wordle game."""

__author__ = "730738053"


def input_guess(secret_word_len: int) -> str:
    """Prompting a guess for the secret word."""
    word: str = input(f"Enter a {secret_word_len} character word: ")
    while len(word) != secret_word_len:
        word = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Determining which characters are in both the guess and the secret word."""
    assert len(char_guess) == 1
    index: int = 0
    match: bool = False
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            match = True  # The return value is changed to true if there is a match.
        index += 1
    return match


def emojified(guess: str, secret: str) -> str:
    """Evaluating the guess relative to the secret with emojis."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    emoji_string: str = (
        ""  # As the letters are checked, the emojis will be added to this string.
    )
    while index < len(secret):
        if guess[index] == secret[index]:
            emoji_string += GREEN_BOX
        elif contains_char(secret, guess[index]) == True:
            emoji_string += YELLOW_BOX
        else:
            emoji_string += WHITE_BOX
        index += 1  # This moves onto the next character.
    return emoji_string


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    guesses_num: int = 1
    while guesses_num < 7:
        print(f"=== Turn {guesses_num}/6 ===")
        guess: str = input_guess(secret_word_len=len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {guesses_num}/6 turns !")
            break
        guesses_num += 1
    if (
        guesses_num > 6
    ):  # If it is not guessed after exiting the while loop, the then block is entered.
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
