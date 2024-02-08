def print_door_mat(rows, cols):
    # Pattern creation
    pattern = [('.|.' * (2 * i + 1)).center(cols, '-') for i in range(rows // 2)]
    welcome = 'WELCOME'.center(cols, '-')
    
    # Print the upper part of the mat
    for line in pattern:
        print(line)
    
    # Print the welcome message
    print(welcome)
    
    # Print the lower part of the mat in reverse order
    for line in reversed(pattern):
        print(line)

# Reading input values
rows, cols = map(int, input().split())

# Printing the door mat
print_door_mat(rows, cols)
