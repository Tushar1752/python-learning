#multiple inheritance is defined as a feature of some object-oriented programming languages in which a class can inherit behaviors and features from more than one parent class. 




class Employee:
    def __init__(self,name):
        self.name=name
class Dancer:
    def __init__(self,style):
        self.style=style
    def __str__(self):
        return f" The name is {self.name} and the dance style is {self.style}"
class DancerEmployee(Employee,Dancer):
    def __init__(self,name,style):
        self.style=style
        self.name=name

a= DancerEmployee("Sufyan","chapri")
print(a)

print(a.name)
print(a.style)
#In this example, the DancerEmployee class inherits from both the Employee and Dancer classes