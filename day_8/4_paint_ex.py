from math import ceil

COVERAGE = 5


def paint_wall(width: float, height: float) -> int:
    return ceil((width * height) / COVERAGE)


print(f"Can required are {paint_wall(5, 3)} Can.")
