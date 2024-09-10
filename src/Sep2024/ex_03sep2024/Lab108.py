# get input from user and create a class

class Person:
    def __init__(self):
        self.name=input("Enter name")
        self.age =input("Enter age")
        self.phone=input("Enter phone")
        self.occupation=input("Enter Occupation")

    def printperson(self) :
        print(f"Name is {self.name}")
        print(f"{self.age}")
        print(f"{self.phone}")
        print(f"{self.occupation}")


person1 =Person()
person1.printperson()

