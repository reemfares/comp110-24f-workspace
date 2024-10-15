def get_first(input: list[str]) -> str:
    if len(input) == 0:
        return ""
    return input[0]


def remove_first(input: list[str]) -> None:
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    first_element: str = input[0]
    input.pop(0)
    return first_element


def test_get_first() -> None:
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    assert get_first(dog_breeds) == "husky"


def test_remove_first_return_value() -> None:
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    assert remove_first(dog_breeds) == None


def test_remove_first_behavior() -> None:
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    remove_first(dog_breeds)
    assert dog_breeds == ["golden", "poodle", "lab"]


def test_get_first_edge_case() -> None:
    assert get_first([]) == ""
