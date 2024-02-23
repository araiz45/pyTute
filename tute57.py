# Introduction to OOPS
# Classes and Objects
class Person:
    name = "araiz"
    occupation = "computer scientist"
    networth = 4
    def info(self):
        print(f"{self.name} is a {self.occupation} and his net worth is {self.networth}")

a = Person()
print(a.name)
a.info()
a.name = "zaid"
print(a.name)
print(a.occupation)
a.occupation = "accoutant"
print(a.occupation)
print(a.networth)
a.info()

b = Person()
b.name = "Human"
b.occupation = "HR"
b.networth = 333
b.info()

c = Person()
c.info()