"""
created by Nagaj at 19/06/2021
"""
from pprint import pprint

import pandas as pd

weather = pd.read_csv("./weather_data.csv")

print(type(weather))

pprint(weather.to_dict())

weather.to_json("weather.json", indent=4)

temps = weather["temp"].tolist()  # with duplicates
print(temps)
print(weather["temp"].unique())  # without duplicates


class WeatherDF:
    TEMP = "temp"
    DAY = "day"
    CONDITION = "condition"

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def has_rows(self):
        return self.dataframe.shape[0] > 0

    def first(self):
        if self.has_rows():
            return self.dataframe.head(1)

    def last(self):
        if self.has_rows():
            return self.dataframe.tail(1)

    @property
    def temps(self):
        return self.dataframe[self.TEMP]

    @property
    def temp_avrg(self):
        return self.dataframe[self.TEMP].mean()

    @property
    def max(self):
        return self.dataframe[self.TEMP].max()

    @property
    def min(self):
        return self.dataframe[self.TEMP].min()

    @property
    def conditions(self):
        return self.dataframe[self.CONDITION]

    @property
    def days(self):
        return self.dataframe[self.DAY]

    def __len__(self):
        return len(self.dataframe)


print(len(weather))
weather = WeatherDF(weather)

print(weather.first())
print(weather.last())

print(len(weather.dataframe))
print(len(weather))

print(weather.temp_avrg)

print(weather.dataframe["temp"].min(), weather.max)
print(weather.dataframe["temp"].max(), weather.min)
print(weather.dataframe["condition"])
print(weather.conditions)

# get data in columns

print("#" * 100)
print(weather.days)
print(weather.dataframe["day"])

for tmp in weather.temps:
    print(tmp)

print("#" * 100)

print(
    weather.dataframe.temp
)  # df.colName  ==> but not recommended because may be col name has spaces

# get data in rows

print("#" * 100)

monday = weather.dataframe[weather.days == "Monday"]  # filter and get rows of Monday

print(monday)

print("#" * 100)

maxs = weather.dataframe[weather.temps == weather.temps.max()]  # rows of max values
print(maxs)

print("#")

sunny = weather.dataframe[weather.conditions == "Sunny"]  # get just sunny days

print(sunny)

# max temp of sunny days

sunny = weather.dataframe[weather.conditions == "Sunny"]
print("#" * 100)
print(sunny["temp"].max(), sunny.temp.max())

# monday's temp from C to F

monday = weather.dataframe[weather.days == "Monday"]
# (0°C × 9/5) + 32

print((monday["temp"] * 9 / 5) + 32)

# create df from scratch
print("#" * 100)

players = [
    {"name": "Salah", "age": 27, "team": "liverpool", "leg": "left"},
    {"name": "Ronaldo", "age": 37, "team": "Juv", "leg": "right"},
    {"name": "Messi", "age": 34, "team": "Barca", "leg": "left"},
]

players_df = pd.DataFrame(players)

print(players_df)

max_age = players_df["age"].max()
print(max_age)  # just number

# find player of max age

max_player = players_df[players_df["age"] == max_age]
print(max_player)

print("#" * 100)

left_leg_players = players_df[players_df["leg"] == "left"]
right_leg_players = players_df[players_df["leg"] != "left"]

print(left_leg_players)
print(right_leg_players)

players_df.to_excel("players.xlsx", sheet_name="players")
