# Input
n = int(input().strip())

# Initialize an empty set to store distinct country stamps
distinct_stamps = set()

# Iterate through the input and add each country stamp to the set
for _ in range(n):
    country_stamp = input().strip()
    distinct_stamps.add(country_stamp)

# Output the total number of distinct country stamps
print(len(distinct_stamps))
