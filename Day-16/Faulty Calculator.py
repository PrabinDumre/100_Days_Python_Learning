print("Enter first number")
o=int(input())
print("Enter second number")
i=int(input())
print("Enter operator")
p = (input())
if (o==45 and i==3 and p=='*'):
    print(555)
elif(o==56 and i==9 and p=='+'):
    print(77)
elif(o==56 and i==6 and p=='/'):
    print(4)
elif p=='*':
    w=o*i
    print(w)
elif p=='+':
    w=o+i
    print(w)
elif p=='-':
    w=o-i
    print(w)
elif p=='/':
    w=o/i
    print(w)
