# input = 34
# output = 3 + 4 = 7

# =====================
# input = 56
# output = 5 + 6 = 11

number = input("Enter Number of 2 digits: ")

output = int(number[0]) + int(number[1])

print(output)

total = sum([int(num) for num in input("Enter number")])
print(total)
