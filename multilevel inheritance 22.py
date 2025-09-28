#multilevel inheritance is defined as a child class derived from a parent class, which is also derived from another parent class.
#multiple inheritance is defined as a child class derived from more than one parent class.
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_details(self):
        return f"{self.name} is a {self.species}"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="dog")   # Call Animal constructor
        self.breed = breed

    def show_details(self):
        parent_details = super().show_details()  # Get details from Animal
        return f"{parent_details}, and is of {self.breed} breed"


class GoldenRetriever(Dog):
    def __init__(self, name, color):
        super().__init__(name, breed="Golden Retriever")  # Call Dog constructor
        self.color = color

    def show_details(self):
        parent_details = super().show_details()  # Get details from Dog
        return f"{parent_details}. It is {self.color} in color"
gr = GoldenRetriever("Buddy", "Golden")
print(gr.show_details())