from string import ascii_letters as letters
from random import choice, sample


print("Welcome to password generator")
numbers = "".join([str(i) for i in range(0, 10)])
symbols = "$#%^&*()!+"

nr_length = int(input("How many letters do you want ?"))
nr_numbers = int(input("How many numbers do you want ?"))
nr_symbols = int(input("How many symbols do you want ?"))

password = ""
for _ in range(nr_length):
    c = choice(letters)
    password += c


for _ in range(nr_numbers):
    num = choice(numbers)
    password += num

for _ in range(nr_symbols):
    symbol = choice(symbols)
    password += symbol

print(password)
pwd: list = sample(password, len(password))
print("".join(pwd))
