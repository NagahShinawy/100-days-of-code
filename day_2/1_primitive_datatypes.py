# print("Hello"[5])
char = "Hello"[5] if 5 in range(len("Hello")) else "Out of index"
print(char)

# todo : subscript means [] ==> like string[0]

# print(123[0])

print("23" + "1")

# todo : large integers

nationalid = 12_354_365_734_512  # 12354365734512 ==>  python ignore _ to visualize number more easily
print(nationalid)

PI = 3.14
salary = 345.55

is_pregnant = True
print("Ps" if is_pregnant else "Ng")

# input (potatoes) ===> processing(making_chips_function) ==> output (chips)
# input (rocks) ===> processing(making_chips_function) ==> output ERROR, because of invalid inputs

print("#" * 20)
num_chars = len(input("Enter name"))

print(type(num_chars))
print()
print(type("test"))
print("Your name has " + str(num_chars) + " chars")  # Type Casting
print(int(123.54345))  # 123
print(float(123))  # 123.0
print(float("123"))  # 123.0
print(int("123"))  # 123
print(70 + float("100.5"))  # 170.5
print("70" + "100")  # 70100
print("Your name has " + num_chars + " chars")  # TypeError: must be str, not int
