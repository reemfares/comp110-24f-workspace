"""My third challenge question of COMP 110."""

__author__ = 730738053


def guess_a_number() -> None:
    """Guess a secret number."""
    secret: int = 7
    number: str = input("Guess a number:")
    print("Your guess was " + number)
    if int(number) == secret:
        print("You got it!")
    elif int(number) < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
