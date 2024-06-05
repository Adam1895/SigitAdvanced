numbers = iter(list(range(1, 101)))

while True:
    try:
        next(numbers)
        next(numbers)
        print(next(numbers))
    except StopIteration:
        break
        