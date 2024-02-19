def average(array):
    distinct_heights = set(array)
    return sum(distinct_heights) / len(distinct_heights)

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = average(arr)
    print("{:.3f}".format(result))
