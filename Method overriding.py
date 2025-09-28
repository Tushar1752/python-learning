#method overriding is when a child class has a method with the same name as a method in the parent class.
#When you call the method on an instance of the child class, the method in the child class is called instead of the method in the parent class.

class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y
rec=Shape(3,19)
print(rec.area())


class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14*self.r*self.r
c=Circle(3)
print(c.area())


