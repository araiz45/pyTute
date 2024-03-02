# Instance Variables vs Class Variables
class Employee:
    companyName = "InternetCo"
    noOfEmployee = 0
    def __init__(self, name):
        self.name = name
        self.pansion = 11
        Employee.noOfEmployee += 1

    def ShowDetails(self):
        print(f"The name of the Employee is {self.name} of company {self.companyName} with staff of {self.noOfEmployee} and pasion is {self.pansion}")


araiz = Employee("araiz")
araiz.companyName = "Human Rights Company (HRC)"
araiz.ShowDetails()

azish = Employee("Azish")
Employee.ShowDetails(azish)