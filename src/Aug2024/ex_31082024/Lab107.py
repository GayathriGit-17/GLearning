class Person:
    # Attributes
    id=None
    name=None
    age=None
    email=None
    height=None
    gender=None
    phone_no=None
    address=None


    # Behavior
    def __init__(self):
        print("Constructors")
    def __init__(self,name):
        print("Constructors")
        self.name=name
    def talk(self): # self is the first argument in every behaviour - No return type and No Argument
        print("I can talk")

    def sleep(self,name):
        print("Iam a Method !")
        print("sleep",name)
    def sleep2(self,name):
        print("Iam a Method")
        return None
    def walk(self):
        print("Iam Walking")

    def walk_return(self):
        return "Iam Walking"


    # create instance

Gayathri = Person("Shan")
#Gayathri.name= "Gayathri"
print(Gayathri.name)

Gayathri1 = Person("G")
Gayathri1.name= "Gayathri"
print(Gayathri1.name)

GayathriS = Person("GS")
GayathriS.name = "GayathriS"
print(GayathriS.name)
"""

#Calling without a argument in constructor
Gayathri1 = Person()
Gayathri1.name= "Gayathri"
print(Gayathri1.name)

GayathriS = Person()
GayathriS.name = "GayathriS"
print(GayathriS.name)

"""