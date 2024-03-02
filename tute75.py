# Single Inheritance

class Animal:
    def __init__(self, name, owner) -> None:
        self.name = name
        self.owner = owner

    def MakeSound(self):
        print(f"{self.name} makes sound")

    
class Cat(Animal):
    def __init__(self, name, owner) -> None:
        super().__init__(name, owner)

    def Meow(self):
        super().MakeSound()
        print(f'Meaw')


a = Cat("Kittey", "Fluffy")
a.Meow()