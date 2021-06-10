"""
created by Nagaj at 19/05/2021
"""
import random
from typing import List
from turtle import Turtle, Screen

from data import turtles_data


def screen_setup():
    screen = Screen()
    screen.setup(width=500, height=400)
    color = screen.textinput(
        title="Make Your Bet", prompt="Type The Color That You Think It Will Win? : "
    )
    return screen, color


def setup_turtles():
    turtles_to_race = []
    for turt in turtles_data:
        t = Turtle(shape=turt["shape"])
        t.penup()
        t.color(turt["color"])
        t.goto(x=turt["position"]["x"], y=turt["position"]["y"])
        turtles_to_race.append(t)
    return turtles_to_race


def turtles_race(race: list):
    stop = 500
    while True:
        for t in race:
            t.forward(random.randint(10, 30))
            if t.xcor() >= stop:
                return t


def race_result(winner: Turtle, user_bet: str):
    if winner.color()[0].lower() == user_bet.lower():
        print("You Win: '{}'".format(user_bet))
    else:
        print("You Lose The Winner is: '{}'".format(winner.color()[0]))


def main():
    screen, user_bet = screen_setup()
    turtles_to_race = setup_turtles()
    winner = turtles_race(turtles_to_race)
    race_result(winner, user_bet)
    screen.exitonclick()


if __name__ == "__main__":
    pass
    # main()


class Race:
    STOP = 230

    def __init__(self, competitors: List[Turtle]):
        self.competitors = competitors
        self.winner = None

    def start_race(self):
        while True:
            for competitor in self.competitors:
                competitor.forward(random.randint(1, 10))
                if competitor.xcor() >= Race.STOP:
                    self.winner = competitor
                    return self.winner

    def race_result(self, user_bet: str):
        winner_color = self.winner.pencolor().lower()
        user_bet = user_bet.lower()
        if winner_color == user_bet:
            print("You Win: '{}'".format(user_bet))
        else:
            print("You Lose The Winner is: '{}'".format(winner_color))


class SetUpTurtles:
    def __init__(self, data: List[dict]):
        self.data = data
        self.competitors = []

    def create(self):
        for competitor in self.data:
            self.add_competitor(competitor)
        return self.competitors

    def add_competitor(self, competitor):
        comp = Turtle(shape=competitor["shape"])
        comp.penup()
        comp.color(competitor["color"])
        comp.goto(x=competitor["position"]["x"], y=competitor["position"]["y"])
        self.competitors.append(comp)


def start():

    # ########## setup screen #############

    screen = Screen()
    screen.setup(width=500, height=400)
    screen.bgcolor("black")
    screen.title("Race")
    user_bet = screen.textinput(
        title="Make Your Bet", prompt="Type The Color That You Think It Will Win? : "
    )

    # ############## race   ############
    turtles = SetUpTurtles(turtles_data)
    competitors = turtles.create()
    race = Race(competitors=competitors)
    race.start_race()
    race.race_result(user_bet)

    # ############ wait click to finish  ##############
    screen.exitonclick()


start()
