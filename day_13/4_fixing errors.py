"""
created by Nagaj at 28/04/2021
"""

UNDER_AGE = 18


_age = int(input("Enter Your Age ?"))

if _age < 18:
    print("under age")

else:
    print(f"You can drive at age {_age}")


age = input("Enter Your Age ?")


if age < 18:  # TypeError: '<' not supported between instances of 'str' and 'int'
    print("You Are Under Age")


else:
    print("Accepted")
