class Employees:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showDetails(self):
        print(F"The name of employee:{self.id} is{self.name}")
e=Employees("Tushar Verma",4000)
e.showDetails()