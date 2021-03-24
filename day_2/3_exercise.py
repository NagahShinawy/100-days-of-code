weight = float(input("Enter Wight : "))
height = float(input("Enter height : "))

# bmi = w / h * h
# ex ==> w=70, h=1.75

BMI = weight / (height ** 2)  # body mass index
BMI2 = weight // (height ** 2)  # body mass index

print(int(BMI))  # 22
print(BMI2)  # 22.0

with open("bmi.txt", "w") as f:
    f.write(f"{weight} / {height} = {BMI}")

# print("" + 1)  # TypeError: must be str, not int
