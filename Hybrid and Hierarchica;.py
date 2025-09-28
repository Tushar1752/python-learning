#Hybrid inheritance is a combination of two or more types of inheritance. It allows a class to inherit features from multiple parent classes, which can themselves be derived from other classes. This creates a complex hierarchy that combines the benefits of different inheritance types.       
#Example of Hybrid Inheritance in Python

class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Person(Human):
    def __init__(self,name,age,address):
        Human.__init__(self,name,age)
        self.address=address
    def show_details(self):
        Human.show_details(self)
        print(f"Address:{self.address}")
class Program:
    def __init__(self,program_name,duration):
        self.program_name=program_name
        self.duration=duration
    def show_details(self):
        print(f"Program Name: {self.program_name}, Duration: {self.duration}")
class Student(Person):
    def __init__(self,name,age,address,program):
        Person.__init__(self,name,age,address)
        self.program=program
    def show_details(self):
        Person.show_details(self)
        self.program.show_details()
Program=Program("Computer Science ",5)
Student=Student("tushar",21,"Lucknow",Program)
Student.show_details()




#Hierarchical inheritance is a type of inheritance where multiple derived classes inherit from a single base class. This allows for the creation of a class hierarchy where different subclasses can share common attributes and methods from the base class while also having their own unique features.
#Example of Hierarchical Inheritance in Python  


class Animal:
    def __init__(self,name):
        self.name=name
    def show_details(self):
        print(f"Animal Name: {self.name}")
class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name)
        self.breed=breed
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
class Cat(Animal):
    def __init__(self,name,color):
        Animal.__init__(self,name)
        self.color=color
    def show_details(self):
        Animal.show_details(self)
        print(f"Color: {self.color}")

Dog=Dog("Buddy","pet bull")
Dog.show_details()
Cat=Cat("Whiskers","White")
Cat.show_details()