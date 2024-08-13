#calculator program

number1 = int(input("Enter your number 1"))
number2 = int(input("Enter your number 2"))

usum= number1 + number2
Difference = number1 - number2
product = number1 * number2
quotient = number1 / number2

print(usum)
print(Difference)
print(product)
print(quotient)

# to print upto 4 decimal places
number = 3.14159876
Format_number = f"{number:.4f}"
print( "The number is "f"{number:.4f}")
print(Format_number)   # rounding off happens if => 5


#Printing math table

table =  9
print(f"{table} * 1 = {table}")
print(f"{table} * 2 = {table*2}")
print(f"{table} * 3 = {table * 3}")
print(f"{table} * 4 = {table * 4 }")
print(f"{table} * 5 = {table * 5 }")
print(f"{table} * 6 = {table * 6 }")