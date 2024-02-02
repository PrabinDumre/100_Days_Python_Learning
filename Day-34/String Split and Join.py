def split_and_join(line):
    # Split the input line on spaces and join using a hyphen
    result = "-".join(line.split(" "))
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
