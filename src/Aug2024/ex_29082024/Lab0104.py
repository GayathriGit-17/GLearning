#Dict -key and value combination , used like set

student_inform= {"name" : "Gayathri" ,
                 "Age"  : 10,
                 "Address" : "Bangalore"}

student_inform1= {"name" : "S" ,
                 "Age"  : 12,
                 "Address" : "Chennai"}

print(student_inform)
#print(student_inform[0])
student_inform["age"]=100
student_list = student_inform + student_inform1
print(student_list)

student_inform_dict= dict(name="Gayathri",Age=10,address="Bangalore")
print(student_inform_dict)

