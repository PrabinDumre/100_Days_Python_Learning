from itertools import combinations

# Read input
s, k = input().split()
s = sorted(s)  # Sort the string

# Print combinations
for i in range(1, int(k) + 1):
    for comb in combinations(s, i):
        print(''.join(comb))
