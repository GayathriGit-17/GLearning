my_list=[1,2,3]
my_list[0]="Gayathri"
my_list.append("Shanmugam")
print(my_list)
my_list[3]="S"
print(my_list)
my_list.extend([4,5,6])
print(my_list)
print(len(my_list))
# extend and append add items at the end
# insert inserts the item in between and shifts all the items in the list to one position
my_list.insert(1,"S")
print(my_list)
print(len(my_list))
my_list.insert(-1,"S")
print(my_list)
print(len(my_list))

# remove
my_list.remove(2)
print(my_list)
print(len(my_list))

# copy list

my_list_copy=my_list.copy()
print(my_list)
print(my_list_copy)
my_list.clear()
print(my_list)
print(my_list_copy)

# Sorting can be done if the data types are same in list
my_list.sort()
print(my_list)
print(my_list_copy)

# sorting descending
my_list.sort(reverse=False)
print(my_list)
print(my_list_copy)
# reversing
my_list.reverse()

print(my_list)
print(my_list_copy)

#concatenate 2 lists
l1 =[1,2,3]
l2 =[1,2,3]
l3= l1 + l2
print(l3)

#pop
squares =[1,4,9,16,25]
squares.sort(reverse=True)
print(squares)


print(squares.pop())
print(squares)



