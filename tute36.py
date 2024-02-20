# Enumrates Function in python
marks = [3, 5, 22, 5, 2, 5,2, 5, 2, 5, 3]

index = 0
for mark in marks:
    # print(mark)
    if (index == 3):
        # print("Araiz,")
        pass
    index += 1

# Use Alternative Emmumerate
for index, mark in enumerate(marks):
    # print(mark)
    if (index == 3):
        # print("Horayy")
        pass

str2 = "Aaraiz Baig"
for index, str3 in enumerate(str2, start=1):
    print(str3)
    if (index == 3):
        print("Hey")