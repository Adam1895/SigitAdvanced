from functools import reduce

def is_prime(number):
    return number > 1 and reduce(lambda x, y: x and y, [number % i != 0 for i in range(2, int(number ** 0.5) + 1)], True)


print(is_prime(42))
print(is_prime(43))