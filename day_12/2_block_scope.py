"""
created by Nagaj at 24/04/2021
"""
# 2- there is no block scope in python'

salary = 1000

if salary < 2000:
    salary += 50

print(salary)

enemies = ["Skeleton", "Zombie", "Alien"]

if len(enemies) < 5:
    enemies.append("NEW-ENEMY")
    msg = "new enemy was added"

print(enemies)
print(msg)  # valid name in case of if is True (in that case msg variable is created)


def create_attacker():
    attacker = "ATTACKER"
    if attacker:
        attacker += "-SOMETHING-NEW"
    print(attacker)
    return attacker


# print(
#     attacker
# )  # NameError: name 'attacker' is not defined  (IT IS LOCAL SCOPE WITHIN FUNCTION NO BLOCK SCOPE LIKE IF
create_attacker()
name = "John"
for i in range(2):
    name = "JOHN"

print(name)
