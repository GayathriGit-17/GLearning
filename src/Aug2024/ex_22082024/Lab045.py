# for i in range(0,10):
# print("Gayathri" , i, end="")


my_list = list(range(1, 10))

print(my_list)
for i in range(10, 0, -2):
    print("Gayathri", i, end="")

i = 10
while i:
    print("Gayathri",i)
    i = i - 1
i = 0
while i < 10:
    print("Gayathri",i)
    i = i + 1

    #break and continue
    """

for i in range(1, 10):
    print(i)
    if i == 5:
        break
"""

for j in range(1, 10):

    if j == 5 or j == 6:
        print(j)
    else:
        pass    # no output - no actions to be performed