# class Method

class Employee:
    company = "Microsoft"
    def __init__(self, name) -> None:
        self.name = name

    def show(self):
        print(f"The name of the Employee is {self.name} and company is {self.company}")
    @classmethod    
    def changeClassMethod(cls, company):
        cls.company = company
        

e1 = Employee("Aaraiz")
e1.show()
e1.changeClassMethod("Twitter")
e1.show()
print(Employee.company)