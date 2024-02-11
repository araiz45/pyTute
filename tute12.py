# Switch Case Statement
# x = int(input("Enter the value: "))
x = 4
match x:
    case 0:
        print('the value is zero')
    case 1:
        print("the value is one")
    case _:
        print("the value is other")


y = int(input("Enter the value: "))
match y:
    case _ if y > 0:
        print("Number is positive")
    case _ if y < 0:
        print("Number is Negative")
    case 0:
        print("Number is zero")
    case _:
        print("Not a Number")