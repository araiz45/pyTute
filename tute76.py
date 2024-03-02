# Multiple Inheritance

class Employee:
    def __init__(self, name) -> None:
        self.name = name
    def Show(self):
        print(f"name of the Employee is {self.name}")

class Dancer:
    def __init__(self, dance) -> None:
        self.dance = dance

    def Show(self):
        print(f"name of the Dance is {self.dance}")

class DancerEmployee(Dancer, Employee):
    def __init__(self, name, dance) -> None:
        Employee.__init__(self, name)
        Dancer.__init__(self, dance)
    
    def __str__(self) -> str:
        super().Show()
        return f"{self.name} is do {self.dance} dance"


yasir = DancerEmployee("Yasir", "Break Dance")
print(yasir)
# yasir.Show()