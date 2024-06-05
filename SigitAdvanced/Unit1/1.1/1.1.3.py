def is_divisible_by_four(num):
    return num % 4 == 0

def four_dividers(number):
    return list(filter(is_divisible_by_four, range(1, number + 1)))

print(four_dividers(9))
print(four_dividers(3))