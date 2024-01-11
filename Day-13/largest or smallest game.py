largest = None
smallest = None
while True:
    num = input("Enter an integer number (or 'done' to exit): ")
    if num == 'done':
        break
    try:
        nums = int(num)
    except:
        print("Invalid input")
        continue
    if largest is None or nums > largest:
        largest = nums
    if smallest is None or nums < smallest:
        smallest = nums

if largest is not None and smallest is not None:
    print("Largest number:", largest)
    print("Smallest number:", smallest)
else:
    print("No valid numbers entered.")