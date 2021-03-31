primes = "2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97."
primes = [int(prime.strip()) for prime in primes[:-1].split(",")]


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return number


def check_prime(number):
    is_prime = True
    for x in range(2, number - 1):
        if number % x == 0:
            is_prime = False
            break
    if is_prime:
        return number
    return False


primes_list = []
for j in range(2, 101):
    prime = check_prime(j)
    if prime:
        primes_list.append(prime)

print(primes)
print(primes_list)
assert primes == primes_list
