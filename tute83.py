# Walrus Operator
# happy = False
# print(happy)
# print(happy:=True)


listItem = list()

while (food := input("Enter food you like?")) != "quit":
    listItem.append(food)

print(listItem)