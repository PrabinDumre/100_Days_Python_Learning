from itertools import permutations

# Taking input
s, k = input().split()

# Generating permutations and sorting them lexicographically
perms = sorted(permutations(s, int(k)))

# Printing permutations line by line
for perm in perms:
    print(''.join(perm))
