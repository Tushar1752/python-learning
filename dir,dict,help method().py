#dir method


x=[1,2,3]
print(dir(x))


#dict method

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p=Person("John",23)
print(p.name)
print(p.__dict__)

#Help Method

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p=Person("John",23)
print(p.name)
print(help(Person))