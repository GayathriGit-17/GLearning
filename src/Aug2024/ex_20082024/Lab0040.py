# max of 3 numbers
num1 = int(input("Enter num1\n"))
num2 = int(input("Enter num2\n"))
num3 = int(input("Enter num3\n"))

if (num1 > num2) and (num1 > num3):
    print(" Num1 is greater ", num1)
elif (num2 > num1) and (num2 > num3):
    print(" Num2 is greater ", num2)
else:
    print("Num3 is greater", num3)
