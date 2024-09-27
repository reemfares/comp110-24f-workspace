def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char
    removed."""
    copy: str = ""  # Set up empty str to copy values over
    index: int = 0  # local
    while index < len(msg):
        if msg[index] != char:
            copy += msg[index]  # copy = copy + msg[index]
        index += 1
    return copy


word: str = "yoyo"  # global
print(remove_chars(word, "y"))
print(remove_chars(word, "o"))
