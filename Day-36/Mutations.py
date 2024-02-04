def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
    s = input().strip()
    position, char = input().split()
    position = int(position)
    result = mutate_string(s, position, char)
    print(result)
