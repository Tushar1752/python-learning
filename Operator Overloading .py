#operator Overloading is the ability to define custom behavior for operators in user-defined classes.
#For example, we can define how the + operator behaves when applied to instances of a custom class.
#This is done by defining special methods in the class, such as __add__ for addition, __sub__ for subtraction, and so on.
#Here is an example of operator overloading in Python:

class Vector :
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    def __str__(self):
        return f" {self.i}i +{self.j}j+ {self.k}k"
v1= Vector(3,5,6)
print(v1)



#example 2:


class Vector :
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    def __str__(self):
        return f" {self.i}i +{self.j}j+ {self.k}k"
    def __add__(self,other):
        return Vector(self.i + other.i , self.j + other.j , self.k + other.k)
    def __sub__(self,other):
        return Vector(self.i - other.i,self.j-other.j,self.k-other.k)
v1= Vector(3,5,6)
v2= Vector(1,2,3)
print(v1+v2) #Vector addition using overloaded + operator
print(v1-v2) #Vector subtraction using overloaded - operator
print(type(v1))
print(type(v2))
print(isinstance(v1,Vector))
print(isinstance(v2,Vector))
print(id(v1))
print(id(v2))