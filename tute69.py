# Super Keyword
class Employee:
    def __init__(self, name, ids):
        self.name = name
        self.id = ids

    def HelloEmployee(self):
        print(f"hello employee {self.name} your id is {self.id}")
    

class Programmer(Employee):
    def __init__(self, name, ids, lang):
        super().__init__(name, ids)
        self.lang = lang

    def HelloProgrammer(self):
        super().HelloEmployee()
        print(f"You are a Programmer")


araiz = Employee("araiz", "435")
araiz.HelloEmployee()
araix = Programmer("Araix", "433", "Python")
araix.HelloProgrammer()