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