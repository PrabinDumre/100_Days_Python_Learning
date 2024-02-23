# Read inputs
M = int(input())
set_a = set(map(int, input().split()))
N = int(input())
set_b = set(map(int, input().split()))

# Calculate symmetric difference
symmetric_diff = set_a.symmetric_difference(set_b)

# Print symmetric difference in ascending order
for num in sorted(symmetric_diff):
    print(num)
