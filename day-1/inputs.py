print("Hello " + input("Enter Name:"))  # welcome

name = input("Enter Your Name? : ")

print(name)

names = [name.title() for name in input("Enter names separated by ,").split(',')]

print(names)

degrees = [int(input(f"degree #{i}")) for i in range(1, 4)]  # get degrees from user

total = sum(degrees)

print(degrees)
print(total)

