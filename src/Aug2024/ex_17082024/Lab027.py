import math
#Escape sequence
print("Hello World")
print("Hello\n World") # new line
print("Hello\t World")# tabline
print("Hello \b World") #backspace


#File path store  use r to remove the special meaning of \n , works with single quotes also -r is store as raw string

dir =r"C:\Gayathri\n.txt"

#single quotes inside the string  use "\"

name1 ='Gayathri\'s'
print(name1)
name2= "Gayathri's"
print(name2)


#operators

# divison and mod
#  x//y
# x%y
# x**y

num=divmod(10,2)
print("Divmod")
print(num)
print("//")
print(4//2) # returns the quotient only the integer value ignoring decimal places if any - floor division
print ("%")
print(10%2) # returns the remainder
print("**")
print(4**3)  # 4 is the base and 3 is the power here

#Not operator

iscolorred =True
print(not iscolorred)
print(iscolorred)


x=10
y=20
print (x >y)  # returns false
print (x<y)
print(x==y)

# follows OR gate and AND gate to return the value

f=False
t=True
print(f or t)
print(f and t)

# Not equal to !=

x=10
y=20
result = (x != y)
print (result)


# ternary operator if

my_age = int(input("Enter your age"))

print("I will go Goa" if my_age > 18 else "can't go ,stay home")

# another way of IF

if my_age > 18:
    print("I will go Goa")
else:
    print("can't go ")

    print(math.pi)
    print(math.sin(90))
    print(math.pow(4,3))




