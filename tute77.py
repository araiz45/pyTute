class Animal:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
    
    def showDetails(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
    

class Dog(Animal):
    def __init__(self, name, breed) -> None:
        super().__init__(name, species="Dog")
        self.breed = breed

    def showDetails(self):
        Animal.showDetails(self)
        print(f"Breed: {self.breed}")

    
class GermanShapherd(Dog):
    def __init__(self, name, color) -> None:
        super().__init__(name, breed="German Shapherd")
        self.color = color
    
    def showDetails(self):
        Dog.showDetails(self)
        print(f"Color: {self.color}")


tommy = GermanShapherd("Tommy", "Brown")
tommy.showDetails()
print(GermanShapherd.mro())