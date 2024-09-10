# try ,except and finally

try:
    a = int(input("Enter num a"))  # Value error : invalid literal for int() when user gives string instead of integer
    b = int(input("Enter num b"))
    c = a / b                     # zero division error : division by zero
    print("The result c is", c)
except ValueError as e:
   # print(e)
    print("Please enter valid integer")
except ZeroDivisionError as z:
    print("Zero division error")
else:
    print(f"Result is{c}")
finally:
    print("Finally")  # will be printed if exception occurs or not occurs
print("End of the program")

