# Instance Variables vs Class Variables
class Employee:
    companyName = "InternetCo"
    def __init__(self, name):
        self.name = name
        self.pansion = 11

    def ShowDetails(self):
        print(f"The name of the Employee is {self.name} of company {self.companyName} and pasion is {self.pansion}")


araiz = Employee("araiz")
araiz.companyName = "Human Rights Company (HRC)"
araiz.ShowDetails()

azish = Employee("Azish")
Employee.ShowDetails(azish)