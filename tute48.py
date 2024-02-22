methodToOpen = input("Enter Mode: ")
if (methodToOpen == "r"):
    with open("araiz.py", 'r') as f:
        text = f.read()
        print(text)
elif(methodToOpen == "w"):
    textToWrite = input("Enter Text you want to write: ")
    with open("araiz.py", 'w') as f:
        f.write(textToWrite)
elif(methodToOpen == "a"):
    textToWrite = input("Enter Text you want to write: ")
    with open("araiz.py", 'a') as f:
        f.write(textToWrite)
else:
    print("Invalid Mode")