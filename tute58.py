# Constructor

class Person:
    def __init__(self, constructorArgumentName, constructorArgumentOccupation):
        self.name = constructorArgumentName
        self.occupation = constructorArgumentOccupation
    def info(self):
        print(f"{self.name} is a {self.occupation}")

aaraiz = Person("aaraiz", "computer scientist")
yasir = Person("yasir", "developer")
injir = Person("injir", "hobbist")
aaraiz.info()
yasir.info()
injir.info()