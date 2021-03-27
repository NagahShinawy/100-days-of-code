# don't use sum or len

students_heights = [int(height) for height in input("Enter Heights").split()]

total_heights = 0
length = 0

for height in students_heights:
    length += 1
    total_heights += height

avg = round((total_heights / length), 2)
print(students_heights)
print(total_heights)
print(length)
print(avg)
