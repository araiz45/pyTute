# Inheritance

class Employee:
    def __init__(self, employeeNameArg, employeeSalaryArg):
        self.employeeName = employeeNameArg
        self.employeeSalary = employeeSalaryArg

    def ShowDetails(self):
        print(f"The Employee name is {self.employeeName} and his salary is {self.employeeSalary}")
    
class Programmer(Employee):
    def __init__(self, employeeNameArg, employeeSalaryArg, programmerLangArg):
        super().__init__(employeeNameArg, employeeSalaryArg)
        self.programmerLang = programmerLangArg
    def ShowLang(self):
        print(f"The Programming Language of {self.employeeName} is {self.programmerLang}")


imran = Employee("Imran", 4433)
imran.ShowDetails()
injir = Programmer("Injir", 4433, "Java")
injir.ShowDetails()
injir.ShowLang()
pashto = Employee("Pasto Khan", 4433)
pashto.ShowDetails()