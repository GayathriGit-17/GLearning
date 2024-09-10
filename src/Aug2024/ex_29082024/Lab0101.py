# SET - collection of unique items

# {}

# as SET has unique items , to remove duplicates in list we can covert them to set

t= ["Gayathri","S","Gayathri","S"]
print(set(t))

# union , intersection , difference in SET

s1={1,2,3,4,7}
s2={5,6,7,8}
my_set =s1.union(s2)
print(my_set)
my_set =s1.intersection(s2)
print(my_set)
my_set=s1.issubset(s2)
print(my_set)
for i in s1:
    print(i)
    s1.add(9)
    print(my_set)