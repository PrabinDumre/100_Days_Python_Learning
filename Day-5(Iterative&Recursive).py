# ITERATIVE APPROACH

def factorial(n):
    fact = 1
    for i in range(n):
        fact = fact * (i+1)
    return fact


n = int(input("ENter a number\n"))
print(factorial(n))

# RECURSIVE APPROACH

def factorial(p):
    if p ==  1:
        return 1
    else:
        return p*factorial(p-1)
p = int(input("ENter a number\n"))
print(factorial(p))
