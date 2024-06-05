def parse_ranges(ranges_string):
    def split_ranges():
        for r in ranges_string.split(','):
            start, stop = map(int, r.split('-'))
            yield start, stop

    def expand_range(start, stop):
        for num in range(start, stop+1):
            yield num

    return (num for r in split_ranges() for num in expand_range(*r))



print(list(parse_ranges("1-2,4-4,8-10")))
print(list(parse_ranges("0-0,4-8,20-21,43-45")))
