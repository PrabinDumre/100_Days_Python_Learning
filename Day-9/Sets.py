

s_from_list = set([1,2,3,4,5])
print(s_from_list)
# OR
p=([1,2,5])
s_from_list = set(p)
print(s_from_list)

# To print empty set
s = set()
print(type(s))

# methods of set

# To add element in set
s.add(1)
s.add(2)
print(s)
# To add union of set
s1 = s.union({1,2,3,4})
print(s,s1)
# Intersection of set
s1 = s.intersection({1,2,4})
print(s1)
# To remove
s1.remove(2)
print(s1)

# To check disjoint set
s1 = {4,5,6}
print(s.isdisjoint(s1))