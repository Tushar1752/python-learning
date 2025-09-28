#Use of dunder method __len__

class Employee:
    name="Tushar"
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
e=Employee()
print(len(e))
print(e.name)


#use of str and repr dunder method


class Employee:
    name="Tushar"
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i


    def __str__(self):
       return f"Employee name is {self.name} str"
    
e=Employee()
print(len(e))
print(e.name)
print(e)  #it will call str method


#use of repr dunder method

class Employee:
    name="Tushar"
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i


    def __repr__(self):
       return f"Employee name is {self.name} repr"
    
e=Employee()
print(len(e))
print(e.name)
print(e)  #it will call repr method

#use of call method :


class Employee:
    name="Tushar"
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    def __repr__(self):
       return f"Employee name is {self.name} repr"
    def __call__(self):
       return f"This is call method"
    
e=Employee()
print(len(e))
print(e())