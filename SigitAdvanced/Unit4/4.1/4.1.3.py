import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_generator(start):
    num = start
    while True:
        num += 1
        if is_prime(num):
            yield num

def first_prime_over(n):
    return next(prime_generator(n))

print(first_prime_over(1000000))

