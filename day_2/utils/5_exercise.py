bill = float(input("What is the total bill$"))
tip = int(input("What is the percentage 10, 12 or 15?"))
people = int(input("How many people"))
result = (bill + (tip * bill / 100)) / people

print("Each Person should pay: ${}".format(round(result, 2)))
