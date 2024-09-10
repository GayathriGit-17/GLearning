#result=lambda a,b,c : a+b+c
#print(result(1,2,3))
import math

check_even_odd =lambda num : "Even" if num % 2 == 0 else "Odd"
print(check_even_odd(10))

op2 = lambda  : math.pow(int(input("Enter number\n")),2)
print(op2())
