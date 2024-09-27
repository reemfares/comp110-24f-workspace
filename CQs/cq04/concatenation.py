"""Define a function to import into visualize."""

__author__ = 730738053


def concat(str1: str, str2: str) -> str:
    """Concatenate two strings."""
    return str1 + str2


word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":
    print(concat(word1, word2))
