from itertools import combinations

bills = ([20] * 3) + ([10] * 5) + ([5] * 2) + ([1] * 5 )

combos = []
for i in range(1, len(bills) + 1):
    for combo in combinations(bills, i):
        if sum(combo) == 100:
            combo = tuple(sorted(combo, reverse=True))
            if combo not in combos:
                combos.append(combo)

for combo in combos:
    print(combo)

print(f"Num of options: {len(combos)}")