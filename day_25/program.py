"""
created by Nagaj at 19/06/2021
"""
import pandas as pd
from prettytable import PrettyTable


USED_COLS = ["Primary Fur Color"]
GRAY = "Gray"
BLACK = "Black"
CINNAMON = "Cinnamon"
COLORS = [GRAY, BLACK, CINNAMON]

central_park = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")[
    USED_COLS
]


def to_prettytable():
    table = PrettyTable()
    return table


def main():
    squirrels_by_color = to_prettytable()
    counts = dict()
    by_colors = []
    for color in COLORS:
        squirrels = central_park[central_park["Primary Fur Color"] == color]
        counts.update({color: squirrels.shape[0]})
        by_colors.append({"color": color, "counts": squirrels.shape[0]})  # way 2
    counts = sorted(counts.items(), key=lambda item: item[-1])

    print(counts)
    cols = [item[0].upper() for item in counts]
    row = [item[1] for item in counts]
    squirrels_by_color.field_names = cols
    squirrels_by_color.add_row(row)
    print(squirrels_by_color)
    #########################
    squirrels_by_color_df = pd.DataFrame(by_colors)
    squirrels_by_color_df.to_excel("squirrels_by_color.xlsx")
    print(f"All Rows:{central_park.shape[0]}")


if __name__ == "__main__":
    main()
