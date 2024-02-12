def print_rangoli(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    pattern = []

    # Build the pattern for the upper half
    for i in range(size):
        line = '-'.join(alphabet[size - 1:i:-1] + alphabet[i:size])
        pattern.append(line.center(4 * size - 3, '-'))

    # Print each line in reverse order for the right half of the rangoli
    for line in pattern[::-1]:
        print(line)

    # Print each line in the correct order for the left half of the rangoli
    for line in pattern[1:]:
        print(line)

if __name__ == '__main__':
    size = int(input().strip())
    print_rangoli(size)
