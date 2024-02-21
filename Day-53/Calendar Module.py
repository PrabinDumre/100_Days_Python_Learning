import datetime

# Function to get the day of the week
def find_day(month, day, year):
    # Parse the input date
    input_date = datetime.datetime.strptime(f"{year}-{month}-{day}", "%Y-%m-%d")
    # Get the day of the week
    day_of_week = input_date.strftime("%A").upper()
    return day_of_week

# Reading input
month, day, year = input().split()

# Output the day of the week
print(find_day(month, day, year))
