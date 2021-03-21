from constant import NEWLINE, SPACE

city = input("Enter Your City: ")
pet = input("Enter Your Pet: ")

if len(city) > 3 and len(pet) > 3:
    print(f"You Band Name is {city} {pet}")
    print("You Band Name is {} {}".format(city, pet))
    print(f"You Band Name is {city} {pet}".format(city=city, pet=pet))

emails = [
    "john@lean.com",
    "eric@lean.com",
    "loen@lean.com",
    "smith@lean.com",
]

emails = ";".join(emails)

print(emails)

colors = {"red": "#2323", "green": "#43434", "black": "#42342"}

print("Hello World")

print("What's Your Name ?")
print("What's Your Name ?")

print("Server Info:\n\tHost:google.com\n\tport:8000\n\tdb:mysql")

print("#" * 20)

print(
    f"Server Info:{NEWLINE}{SPACE}Host:google.com{NEWLINE}{SPACE}port:8000{NEWLINE}{SPACE}db:mysql"
)

print("Hello " + pet)
print("Hello" + " " + pet)

print("#" * 20)

print(f"Profile:{NEWLINE}{SPACE}Name: Nagah{NEWLINE}{SPACE}DOB: 23-09-2002")

print("#" * 20)

print('String concat "+" test')
