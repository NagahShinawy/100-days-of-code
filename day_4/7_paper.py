from random import randint

ROCK = """
.-.________
----/ )_______)
(  (/()___)
 ()__)
  ----___()_)

"""


PAPER = """
 ________.-.                
  (_______( / ----      
     (___())  )            
      (__()                     
       (_()___/----     

"""

SCISSOR = '''
      ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'   
'''

game_images = [ROCK, PAPER, SCISSOR]

user_choice = int(input("Type 0 for Rock, 1 for Paper, 2 for scissor"))
user_game_image = game_images[user_choice]
print("You Chose ({}) {}".format(user_choice, user_game_image))
pc_choice = randint(0, 2)
pc_game_image = game_images[pc_choice]
print("Computer Choice is ({}) {}".format(pc_choice, pc_game_image))

if user_choice >= 3 or user_choice < 0:  # not in choices (0, 1, 2)
    print(f"You Types Invalid Number ({user_choice}), You lose")

elif user_choice == 0 and pc_choice == 2:
    print("User Wins")
elif user_choice == 2 and pc_choice == 0:
    print("You Lose#")
elif pc_choice > user_choice:
    print("You Lose")
elif user_choice > pc_choice:
    print("You Win")
elif pc_choice == user_choice:
    print("It's A draw")
