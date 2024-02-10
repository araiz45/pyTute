# Excercise 1 : Calculator
num1 = int(input("Enter Your First Number: "))
num2 = int(input ("Enter Your Second Number: "))
oper = input("Enter Operator: ")

if(oper == "+"):
    print("The sum of num1 and num2 is: ", num1 + num2)
elif (oper == "-"):
    print("The sub of num1 and num2 is: ", num1 - num2)
elif (oper == "*"):
    print("The multi of num1 and num2 is: ", num1 * num2)
elif (oper == "/"):
    print("The divide of num1 and num2 is: ", num1 / num2)
elif (oper == "%"):
    print("The modulus of num1 and num2 is: ", num1 % num2)
elif (oper == "//"):
    print("The floar division of num1 and num2 is: ", num1 // num2)
elif (oper == "**"):
    print("Num1 is base and num2 is power Result: ", num1 ** num2)
else:
    print("Nothing is here")