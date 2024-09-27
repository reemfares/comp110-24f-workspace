"""Create coordinates for strings."""

__author__ = 730738053


def get_coords(xs: str, ys: str) -> None:
    index_x: int = 0
    while index_x < len(xs):
        index_y: int = 0
        while index_y < len(ys):
            print(
                "(" + xs[index_x] + "," + ys[index_y] + ")"
            )  # you could use an f function
            index_y += 1
        index_x += 1
