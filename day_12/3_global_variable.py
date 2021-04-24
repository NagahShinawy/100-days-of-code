"""
created by Nagaj at 24/04/2021
"""

salary = 1000


# using local scope
def update_salary_local_scope():
    salary = 2000
    print(salary)


print(salary)
update_salary_local_scope()
print(salary)

print("#" * 100)
# ########### ########### ########### ########### ########### ########### ########### ##########

salary = 5000
bonus = 10


def update_salary_global_scope():
    global salary
    # bonus = 0 # ERROR : SyntaxError: name 'bonus' is assigned to before global declaration
    global bonus
    bonus += 5
    salary = 8000
    print("Salary Within Function", salary)
    print("inside", bonus)


print("Salary Outside Function", salary)
update_salary_global_scope()
print("Salary Outside Function", salary)
print("Outside", bonus)

print("#" * 100)
# ########### ########### ########### ########### ########### ########### ########### ##########

# update global var without using global

name = "john"


def fullname():
    print("You are updating name")
    # name = name + " " + "james"  # UnboundLocalError: local variable 'name' referenced before assignment
    update_name = name + " " + "James"
    return update_name


print(name)
name = fullname()
print(name)
