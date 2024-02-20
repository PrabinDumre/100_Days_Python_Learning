from collections import defaultdict

# Read input
n, m = map(int, input().split())
group_a = defaultdict(list)

# Populate group A
for i in range(1, n + 1):
    word = input().strip()
    group_a[word].append(i)

# Process group B
for _ in range(m):
    word = input().strip()
    if word in group_a:
        print(" ".join(map(str, group_a[word])))
    else:
        print(-1)
