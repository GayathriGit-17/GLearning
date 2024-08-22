"""
Task #2

Create a program , take 2 inputs from the user num1, num2 and give them
max
pow num1 to num2
sub, mul, sum, div.
Format your out with f{""}

"""

   #  mathemetical functions

#calculator program

number1 = int(input("Enter your number 1"))
number2 = int(input("Enter your number 2"))

max_value =max(number1,number2)
Power_value = pow(number1,number2)
usum= number1 + number2
Difference = number1 - number2
product = number1 * number2
quotient = number1 / number2

print(max_value)
print(Power_value)
print(usum)
print(Difference)
print(product)
print(f"{quotient:.2f}")