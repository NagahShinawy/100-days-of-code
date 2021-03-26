from random import randint, random, uniform

print(randint(1, 10))  # int random

randoms = [randint(20, 30) for num in range(5)]

print(randoms)

# #######################################

print(
    random()
)  # random value from 0.0 to 1.0 (not including 1) ==> .999999999999999 (the max)

print(uniform(3, 6))  # random floating point value from start(3) to end(6)
print(
    round(uniform(10, 20), 2)
)  # random floating point value from start(10) to end(20) with round 2

lover_score = randint(1, 100)
print("Your Love Score is {}".format(lover_score))
