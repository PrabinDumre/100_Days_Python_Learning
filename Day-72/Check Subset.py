def is_subset(A, B):
    return A.issubset(B)

T = int(input().strip())

for _ in range(T):
    input()
    set_A = set(map(int, input().split()))

    input()
    set_B = set(map(int, input().split()))

    print(is_subset(set_A, set_B))
