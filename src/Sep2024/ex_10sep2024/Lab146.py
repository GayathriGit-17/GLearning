#Exceptions
print("start of the program")
try:
    a = int(input("Enter num a"))  # Value error : invalid literal for int() when user gives string instead of integer
    b = int(input("Enter num b"))
    c = a / b                     # zero division error : division by zero
    print("The result c is", c)
except Exception as e:
   # print(e)
    print("Please enter valid integer")
print("End of the program")

