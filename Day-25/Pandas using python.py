import pandas as pd

with open("names.txt") as file:
    names = file.read().splitlines

first_names = [name.split()[0] for name in names]
last_names = [name.split()[1] for name in names]

employee_ids = [f"Emp{i:04d}" for i in range(2320001, 2321001)]
emails = [f"{first_name.lower()}.{last_name.lower()}@jainuniversity.ac.in" for first_name, last_name in zip(first_names, last_names)]
passwords = ["".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789$#@!*&") for _ in range(10)]) for _ in range(1000)]
otps = [random.randint(100000, 999999) for _ in range(1000)]
data = {
    "Employee ID": employee_ids,
    "Names":names,
    "Email": emails,
    "Password": passwords,
    "OTP": otps
}
df = pd.DataFrame(data)

df.to_csv("employee_data.csv", index=False)
print(df.head()
s

# Creating a dictionary with Employee ID, Email, and Password
data = {'Employee ID': employee_ids,
        'Email ID': emails,
        'Password': passwords}

# Creating a Pandas DataFrame
df = pd.DataFrame(data)

# Printing the first 5 rows of the DataFrame
print(df.head())

# Printing the first 2 rows
print(df.head(2))

# Printing the last 3 rows
print(df.tail(3))

# Printing the shape of the DataFrame
print("Shape of DataFrame: ", df.shape)

# Printing the data-types of each column
print(df.dtypes)