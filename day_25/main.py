"""
created by Nagaj at 19/06/2021
"""
import csv
from collections import namedtuple
from prettytable import PrettyTable


WEATHER_COLS = ["DAY", "TEMP", "CONDITION"]

Weather = namedtuple("Weather", ["day", "temp", "condition"])


def lines(filepath):
    with open(filepath, "r") as csvfile:
        return [line.strip() for line in csvfile.readlines()[1:]]


def to_prettytable(cols, rows):
    table = PrettyTable()
    table.field_names = cols
    table.add_rows(rows)
    return table


def readcsv(filepath):
    data = csv.reader(open(filepath))
    return data


def printcsv(rows):
    for row in rows:
        weather = Weather(*row)
        print(f"{weather.day}-{weather.temp}-{weather.condition}")


def main():
    lns = lines(f"./weather_data.csv")
    lns = [line.split(",") for line in lns]
    weather = to_prettytable(WEATHER_COLS, lns)
    print(weather)


if __name__ == "__main__":
    # main()
    printcsv(readcsv("./weather_data.csv"))
