# 1. Print the longest name in the file
with open('names.txt') as file:
    print(max(file, key=len).strip())

# 2. Print the sum of the lengths of all names in the file
with open('names.txt') as file:
    print(sum(len(line.strip()) for line in file))

# 3. Print the shortest names in the file, one per line
with open('names.txt') as file:
    names = [line.strip() for line in file]
    min_length = min(map(len, names))
    print('\n'.join(name for name in names if len(name) == min_length))

# 4. Create a new file with the length of each name, one per line
with open('names.txt') as inp, open('name_length.txt', 'w') as out:
    out.write('\n'.join(str(len(line.strip())) for line in inp))

# 5. Prompt user for length and print names of that length
length = int(input("Enter name length: "))
with open('names.txt') as file:
    print('\n'.join(line.strip() for line in file if len(line.strip()) == length))