# Arguments in Python 
# Function with required arguments
def average(a, b):
    print("The average is ", (a + b) / 2)

average(2, 4)
# Function with default arguments
def average(a = 3, b = 2):
    print("The average is ", (a + b) / 2)

average(33, 11)
# Function with giving first argument and left everything else as default
average(33)
# Function with giving second argument and left every argument as default
average(b = 33)
# Keyword Argument 
average(b = 33, a = 33)
# Function Argument as Tuple
def average(*number):
    print(number)
    sum = 0
    for i in number:
        sum = sum + i
    print("Average of Tuple is ", sum / len (number))
    
average(4, 5, 23, 5, 23)
# Function Argument as Dictionary
def nameing(**name):
    print(name)
    print(f"my name is {name["name"]}, My Father name is {name["fname"]} and my roll no is {name["rollno"]}")


nameing(name = "Araiz", fname = "Zahid", rollno="44")
# Function by returing a value
def AreaOfSquare(a):
    return a * a

c = AreaOfSquare(44)
print(c)
