total = 0

for i in range(1, 101):  # from 1 to 100
    total += i

print("Total : {}".format(total))  # 5050


total = 0

for i in range(100, 0, -1):  # from 100 to 1
    total += i

print("Total : {}".format(total))  # 5050


# evens

for even in range(0, 10, 2):
    print(even)

print("#" * 30)
for odd in range(1, 11, 2):
    print(odd)
