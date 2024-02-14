# Functions
def calculateGMean(a, b):
    geometicMean = (a * b)/(a + b)
    print(geometicMean)


def isGreater(a, b):
    if(a > b):
        print(f"first number a ({b}) is greater than second number b ({a})")
    elif(a == b):
        print(f"first number a ({b}) is equal than second number b ({a})")
    else:
        print(f"first number b ({b}) is greater than second number a ({a})")

# if we want to write after sometime
def isLesser(a, b):
    pass
a = 3
b = 4
# geometicMean = (a * b)/(a + b)
# print(geometicMean)
isGreater(a, b)
calculateGMean(a, b)

c = 4
d = 4
isGreater(c, d)
calculateGMean(c, d)