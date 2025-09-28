#class method as alternative constructor

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
e=Employee("Harry",1000)
print(e.name)
print(e.salary)

string="Harry-1200"
e2=Employee(string.split("-")[0],string.split("-")[1])
print(e2.name)
print(e2.salary)

#now the short alternative of above with the help of class parameter

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])

string="tushar-1000"
e2=Employee.fromStr(string)
print(e2.name)
print(e2.salary)


#another example

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def from_string(cls,string):
        name,age=string.split(",")
        return cls(name,int(age))
person=Person.from_string("Tushar,19")
print(person.name,person.age)


#creating a rectangular object with widt 10 and height 5

class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    @classmethod
    def square(cls,size):
        return cls(size,size)
rectangle=Rectangle.square(10)
print(rectangle.width, rectangle.height)