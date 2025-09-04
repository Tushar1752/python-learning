#Public access modifier

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
obj=Student("tushar",22)
print(obj.name)
print(obj.age)


#private acces modifier

# class Student:
#     def __init__(self,age,name):
#         self.__age=age
#         def __funName(self):
#             self.y=22
#             print(self.y)
# class Subject(Student):
#     pass
# obj=Student(21,"Tushar")
# obj1=Student

# print(obj.__funName())
# print(obj.__age)


#name mangling

class Myclass:
    def __init__(self):
        self._private_attribute="I am private attribute"
        self.__mangled_attribute="I am mangled attribute"
my_object=Myclass()
print(my_object._private_attribute)
print(my_object._Myclass__mangled_attribute)



#protected access modifier

class Student:
    def __init__(self):
        self._name="Tushar"
    def _funName(self):
        return "hatt thari behan ka"
class subject(Student):
    pass
obj=Student()
obj1=subject()
print(obj._name)
print(obj._funName())
print(obj1._name)