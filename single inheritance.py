#Single inheritance in python is a mechanism where a class (child class) inherits properties and behaviors (attributes and methods) from another class (parent class). This allows the child class to reuse code from the parent class, promoting code reusability and a hierarchical relationship between classes 


class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def make_sound(self,sound):
        print("Sound made by "+self.name+" is "+sound)

Dog=Animal("nandu","Dog")
Cat=Animal("Moti","Cat")

Dog.make_sound("Bark")
Cat.make_sound("Meow")