bill = 0
size = input("Enter Your Size S M L")
if size == "S":
    bill += 15
elif size == "M":
    bill += 20

elif size == "L":
    bill += 25

else:
    print(f"Wrong {size}, just [S, M, L]")

add_p = input("Add Pepperoni? Y / N")
extra_chess = input("Extra Cheese Y / N")

if add_p == "Y" and size == "S":
    bill += 2
elif add_p == "Y" and (size == "M" or size == "L"):
    bill += 3


if extra_chess == "Y":
    bill += 1

print("Total Bill $ {}".format(bill))
