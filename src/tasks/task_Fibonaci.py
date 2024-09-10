# Fibonacci series


n=int(input("Enter a limit:"))
a=0
b=1
print(a)
print(b)
for i in range(n-2):
    t=a+b
    print(t)
    c=a
    a=b
    b=t
