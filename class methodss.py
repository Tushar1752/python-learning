class Employee:
    company="Apple"
    def show(self):
        print(f"The name is {self.name} and the company in which working is {self.company}")
    @classmethod
    def changecompany(cls,newcompany):
        cls.company=newcompany
e1=Employee()
e1.name=("Tushar")
print(Employee.company)
e1.show()
e1.changecompany("tesla")
e1.show()
print(Employee.company)