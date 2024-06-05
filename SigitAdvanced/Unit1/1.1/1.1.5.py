from functools import reduce

def add_digits(digit1, digit2):
    return int(digit1) + int(digit2)

def sum_of_digits(number):
    return reduce(add_digits, str(number))

print(sum_of_digits(104))
