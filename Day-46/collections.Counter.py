from collections import Counter

# Step 1: Read input values
num_shoes = int(input())
shoe_sizes = Counter(map(int, input().split()))
num_customers = int(input())

total_earned = 0

# Step 3: Iterate through each customer
for _ in range(num_customers):
    size, price = map(int, input().split())
    
    # Step 4: Check if the desired shoe size is available
    if shoe_sizes[size] > 0:
        total_earned += price
        shoe_sizes[size] -= 1

# Step 5: Print the total earned money
print(total_earned)
