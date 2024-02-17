# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the input values
    a, b = input().split()
    try:
        # Attempt integer division
        result = int(a) // int(b)
        print(result)
    except ZeroDivisionError as e:
        # Handle division by zero error
        print("Error Code:", e)
    except ValueError as e:
        # Handle invalid literal error
        print("Error Code:", e)
