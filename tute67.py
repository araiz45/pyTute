class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @classmethod
    def changeStr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])
    def PrintName(self):
        print(f"employe name is {self.name} and salary is {self.salary}")


araiz = Employee("araiz", 500)
araiz.PrintName()
em1 = "injir-4000"
em1 = Employee.changeStr(em1)
em1.PrintName()