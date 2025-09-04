class Myclass:
    class_variable=0

    def __init__(self):
        Myclass.class_variable +=1
    def print_class_variable(self):
        print(Myclass.class_variable)
obj1=Myclass()
obj2=Myclass()
obj1.print_class_variable
    



#next question

class Employee:
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.2        #this is a intance variable because we can change its value later on
    def showDetails(self):
        print(f"MY name is {self.name} and my raise salary is {self.raise_amount}")
emp1=Employee("Tushar")
emp1.raise_amount=0.8 #this is instance change
emp1.showDetails()
Employee.showDetails(emp1)

emp2=Employee("Rahul")
emp2.showDetails()