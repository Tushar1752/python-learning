# creating a class:
class person:
    name="Tushar"
    occupation="Student"
    age=20 
a=person
print(a.name)


#creating and defining self

class person:
    name="Tushar"
    occupation="Student"
    age=20 
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a=person()
a.info()
    