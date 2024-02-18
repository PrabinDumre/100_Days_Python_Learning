import cmath

# Taking input as a complex number
z = complex(input())

# Calculating modulus (absolute value) and phase (angle)
r = abs(z)
phi = cmath.phase(z)

# Printing the polar coordinates rounded to 3 decimal places
print(round(r, 3))
print(round(phi, 3))
