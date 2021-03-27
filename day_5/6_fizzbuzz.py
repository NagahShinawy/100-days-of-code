FIZZBUZZ = "FizzBuzz"
FIZZ = "Fizz"
BUZZ = "Buzz"

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} is {FIZZBUZZ}")
    elif num % 3 == 0:
        print(f"{num} is {FIZZ}")
    elif num % 5 == 0:
        print(f"{num} is {BUZZ}")
    else:
        print(num)
