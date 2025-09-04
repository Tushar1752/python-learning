class person:
    def __init__(self,n,o):
        print("Hey i am a obedient boy")
        self.name= n
        self.occ=o
    def info(self):
         print(f"{self.name} is a {self.occ} ")
a=person("Tushar","Developer")
b=person("danish","HR")
a.info()
b.info() 


#parameterized constructor

class details:
    def __init__(self,animal,group):
        self.animal=animal
        self.group=group

obj1=details("crab","Crustaceans")
print(obj1.animal,"belong to",obj1.group)


#Default constructor

class Details:
    def __init__(self):
        print("Animal crab belong to the crustaceans")
obj1=Details()