total = 0
evens = []

for even in range(0, 101, 2):
    total += even
    evens.append(even)


print("Evens ", evens)
print(len(evens) == 51)
print("Total Evens", total)

print("#" * 30)

total = 0
for number in range(101):
    if number % 2 == 0:
        total += number

print("Total Evens", total)
