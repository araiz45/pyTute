# Access Modifiers
# Public Modifier
class Employee: 
    def __init__(self):
        self.name = "Araiz"
    
a = Employee()
print(a.name)
# Private Modifier
class Employee: 
    def __init__(self):
        self.__name = "Araiz"
    
a = Employee()
# print(a.__name) # This returns error
# Accessing Private Key
print(a._Employee__name) # name mangaling
print(a.__dir__()) # Give all the methods which is avaliable

# Protected 
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def _funName(self):
        return "Araiz is good boy"
    

class Asian(Person):
    pass


john = Person("John", 44)
insan = Person("Insane", 55)
print(john._funName())
print(insan._funName())
