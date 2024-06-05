from functools import reduce

def is_funny(string):
    return reduce(lambda x, y: x and (y in 'ha'), string, True)

print(is_funny("hahahahahaha"))
