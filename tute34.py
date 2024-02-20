# Raising error
a = input("Enter any value between 5 to 9: ")
if(a != "quit"):
    a = int(a)
    if(a < 5 or a > 9):
        raise ValueError("Value should be 5 and 9")
    else:
        print("no problem")
else:
    print("quit")
