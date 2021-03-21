from constant import DIE_DICE, UNDER_AGE
from die_dice import Number


number = Number(5)
is_valid = number.is_valid()


num = number.to_int()
num_as_literal = DIE_DICE[num]
print(num, num_as_literal)
print(number.is_odd())
print(number.is_even())

if num < UNDER_AGE:
    print("Age is under age")
else:
    print("Accepted")