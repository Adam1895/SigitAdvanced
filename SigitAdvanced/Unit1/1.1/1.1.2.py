from functools import reduce

def double_char(accumulated, char):
    return accumulated + char + char

def double_letter(my_str):
    return reduce(double_char, my_str, '')

print(double_letter("python"))
print(double_letter("we are the champions!"))