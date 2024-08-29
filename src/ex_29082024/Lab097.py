squares =[1,4,9,16,25]
squares.sort(reverse=True)
print(squares)


print(squares.pop())
print(squares)

# List is Mutable in nature i.e they can change but Tuples are imutable in nature i.e cannot change

# Tuple -collection of items

my_tuple =("G","S")
# my_tuple[0]="D" # not allowed
print(my_tuple)

# converting list to tuple and vice versa
my_list=list(my_tuple)
print(my_list)
my_tuple=tuple(my_list)
print(my_tuple)
# convert list to tuple - note it contains a list indicated by "["
t1 =tuple(["G","S"])
#print(t1(0))
# search in Tuples
cities =("Germany","Italy","India")
print("India" in cities)