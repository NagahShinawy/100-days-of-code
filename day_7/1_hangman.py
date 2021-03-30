# from replit import clear , clear the screen like clear in linux or cls in windows (python 3.8)
import os
from random import choice
from word_list import words
from stages_list import stages


def clear():
    os.system("cls")


word = choice(words)
word_len = len(word)

display = ["-"] * word_len
print(display)


def user_guess():
    guess = input("Enter Letter")
    clear()  # clear screen
    if guess in display:
        print(f"You have already guessed this char '{guess}'")
    for index in range(word_len):
        letter = word[index]
        if letter == guess:
            display[index] = letter
    print(display)
    return guess


lives = len(
    stages
)  # you have 5 lives , you have 5 tries , every try means lose a stage (stages len)
end_of_game = False
stage_index = 0
while not end_of_game:
    g = user_guess()
    if "-" not in display:
        print("You Win", "".join(display))
        end_of_game = True
    if g not in word:
        print(f'"{g}" is not in word. You lose a life')
        lives -= 1
        print(stages[stage_index])
        stage_index += 1
    if lives == 0:
        print("You lose")
        end_of_game = True
