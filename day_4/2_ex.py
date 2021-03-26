from random import random, seed, choice, randint
from string import ascii_letters

# test_seed = int(input("Create a seed number"))  # 123
# seed(test_seed)  # make the random number is always the same value

num = random()  # if test_seed = 123 ==> random is always value (0.052363598850944326),
# if test_seed = 321 ===> random is always value (0.2754594638268887)


def head_tails():
    testseed = int(input("Create a seed number"))  # 123
    seed(testseed)  # make the random number is always the same value
    # for ex: if you choose testseed = 10, and random_side is 0, then the random_side is ALWAYS 0 if you choose 10
    random_side = randint(0, 1)
    print("Side", random_side)
    if random_side:
        print("Heads")
    else:
        print("Tails")


print(num)


def generate_letter():
    # ascii_letters = ascii_lowercase + ascii_uppercase
    alphabetical = ascii_letters
    return choice(alphabetical)


head_tails()
# chars = [generate_letter() for _ in range(10)]
# print(chars)

# 0.2754594638268887
