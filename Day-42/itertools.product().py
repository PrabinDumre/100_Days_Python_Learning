from itertools import product

# Read input lists
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Compute cartesian product
cartesian_product = list(product(A, B))

# Sort the cartesian product
cartesian_product.sort()

# Output the cartesian product
for item in cartesian_product:
    print(item, end=' ')
