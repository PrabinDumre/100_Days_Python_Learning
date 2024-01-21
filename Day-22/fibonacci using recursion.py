def fibo(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        fib = fibo(n-1)+fibo(n-2)
        p = fib
    return p
n = int(input("Enter a  number which you want to print "))
print(fibo(n))