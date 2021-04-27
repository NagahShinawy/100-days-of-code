"""
created by Nagaj at 27/04/2021
"""

year = int(input("What is Your Year Of Birth ?"))

# try missing 1994

# bad way

if year > 1980 and year < 1994:
    print("1-Millenial")

elif year > 1994:
    print("1-Gen Z")

# good way CHAIN OPERATORS: (LARGER THAN AND SMALLER THAN)

if 1980 < year < 1994:
    print("2-Millenial")

elif year > 1994:
    print("2-Gen Z")

if year in range(1981, 1994):
    print("3-Millenial")

elif year > 1994:
    print("3-Gen Z")

# fixing the bug. Include both 1980, 1994

if 1980 <= year < 1994:
    print("4-Millenial")

elif year >= 1994:
    print("4-Gen Z")
