# Nested If else statement
a = int(input("Enter Your Age: "))
if(a > 12): 
    print("You can drive")
    if(a > 15):
        print("you can drive truck")
    else:
        print("You can not drive truck")

else:
    print("you can not drive")
