# Introduction to List
list1 = [2, 4, 2, 3, 5, 3]
list2 = ["Injir", "Pashto", "Kundi", "Lal baig", "Miswar"]
print(list1, list2)
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])
# print(list1[4])
# print(list1[5])
# print(list2[0])
# print(list2[1])
# print(list2[2])
# print(list2[3])
# print(list2[4])
list1[0] = "Azish"
for i in list2:
    print(i)

# List with different dataTypes
list3 = [3, 5, "Injir", "Pista", True]
print(list3)

# Negative Indexing
print(list1[-3])
print(list1[len(list1)-3])
print(6 - 3)
print(list1[3])
# These four lines are same

# Conditional Statement to find is item present in the list 
if 4 in list1:
    print("Yes")

if "Injir" in list2:
    print("YES")
else:
    print("NO")


# Conditional Statement to find is certain string present in the given string

if "iz" in "araiz":
    print("YES FOR STRING")
else:
    print("NO FOR STRING") 


# List Printing
print(list2)
print(list2[:])
print(list2[1:])
print(list2[1: -1])
# the third argument is jump 
print(list2[0: 5: 2]) # it is jumping from 1, 3, 5


# List Comprehension
lst = [l+1 for l in range(5)]
print(lst)

lst = [l+1 for l in range(10) if l % 2 == 0]
print(lst)