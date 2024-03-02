x = (3, 5, 4, 3)
print(dir(x))


class Person:
    def __init__(self) -> None:
        self.name = "omega"
        self.age = 44
        self.version = 2.3

a = Person()
print(a.__dict__)
print(a.__dir__())
print(help(Person))