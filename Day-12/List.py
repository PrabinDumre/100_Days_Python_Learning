Grocery = ["Choco" , "Soap" , "Perfume"]
print(Grocery)
print(Grocery[2]) # By index

num = [2,3,4,5,6]
print(num)
print(num[2])

# To sort number
numb = [2,5,8,7,3,4]
numb.sort()
print(numb)
print(numb[2])

#To Reverse number
numb.reverse()
print(numb)
print(numb[2])

# Slicing element in list
print(num[:])# From start to end
print(num[0:5])# From given start to given end
print(num[1:]) # Exclude first element
print(num[:4]) # Exclude last element

# Positive slicing
print(num[::2]) # By skiping given
# Negative slicing
print(num[::-2]) # By skiping given

# To add in end
num.append(0)
print(num)

# To insert
num.insert(1, 66)
print(num)

# To remove
num.remove(66)
print(num)

# To pop
num.pop()
print(num)

# TUPLE

p = (1,2)
print(p)

# To swap values
a=2
b=3
a,b=b,a
print(a,b)