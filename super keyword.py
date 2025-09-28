class ParentClass:
    def parent_method(self):
        print("This is parent method")
class ChildClass(ParentClass):
    def child_method(self):
        print("This is chid metho0d")
        super().parent_method()
    def child_method(self):
        print("This is child method")
        super().parent_method()
child_object=ChildClass()
child_object.child_method()
child_object.parent_method()


#next program
class Employee:
    def __init__(self,name ,id):
        self.name=name
        self.id=id
class Programmer(Employee):
    def __init__(self,name,id,language):
        super().__init__( name,id)
        self.language=language
rohan=Employee("Rohan","333")
Tushar=Programmer("Tushar","430","Python")
print(rohan.id)
print(Tushar.language)
print(Tushar.id)