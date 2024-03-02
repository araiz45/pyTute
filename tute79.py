# Heiartical inheritance

class Human:
    def __init__(self, name, continent) -> None:
        self.name = name
        self.continent = continent

    def showInfo(self):
        print(f"Name: {self.name}")
        print(f"Continent: {self.continent}")

class Asian(Human):
    def __init__(self, name, country) -> None:
        super().__init__(name, continent="Asian")
        self.country = country

    def showInfo(self):
        Human.showInfo(self)
        print(f"Country: {self.country}")


class European(Human):
    def __init__(self, name, country) -> None:
        super().__init__(name, continent="European")
        self.country = country

    def showInfo(self):
        Human.showInfo()
        print(f"Country: {self.country}")


class African(Human):
    def __init__(self, name, country) -> None:
        super().__init__(name, continent="African")
        self.country = country

    def showInfo(self):
        Human.showInfo()
        print(f"Country: {self.country}")

    
class Australian(Human):
    def __init__(self, name) -> None:
        super().__init__(name, continent="European")
        self.country = "Australia"

    def showInfo(self):
        Human.showInfo()
        print(f"Country: Australia")


class American(Human):
    def __init__(self, name, country) -> None:
        super().__init__(name, continent="American")
        self.country = country

    def showInfo(self):
        Human.showInfo(self)
        print(f"Country: {self.country}")




class Pakistan(Asian):
    def __init__(self, name, city) -> None:
        super().__init__(name, country="Pakistan")
        self.city = city

    def showInfo(self):
        Asian.showInfo(self)
        print(f"City: {self.city}")


araiz = Pakistan("Araiz", "Karachi")
araiz.showInfo()