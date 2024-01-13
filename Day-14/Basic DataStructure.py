# creating a list
number = [1,2,3,4,5]
# Accessing the elements
print("The element in index 1 is:",number[1])
# navigating
for num in number:
    print(num)
#slicing
print("The first three element is:",number[:3])
# adding
number.append(6)
print("The new list is ",number)
#removing last element in list
number.pop()
print(number)
# removing elements from list by value
number.remove(3)
print(number)
#finding length
print("The length is:",len(number))
# inserting
number.insert(2,3)
print("The insert is:",number)


# creating a tuple
number = (1,2,3,4,5)
# Accessing the elements
print("The element in index 1 is:",number[1])
# navigating
for num in number:
    print(num)
#slicing
print("The first three element is:",number[:3])
#finding length
print("The length is:",len(number))
# checkiing
print("3 is in list?",3 in number)
# counting
print("The total is",number.count(3))
#index
print("The index is",number.index(3))

# creating dictionary
person={"name":"Prabin Dumre","age":20,"City":"NP"}
#accessing
print("The name in dictionary is:",person["name"])
#removing
del person["City"]
print(person)
# lenth of dictionary
print("The length is:",len(person))
#adding
person["gender"]="Male"
print(person)
#updating
person["age"]=19
print(person)