# List Methods

list1 = [3, 4, 2, 5]
# Add Values at the end
list1.append(4)
print(list1)
# Start Value in acending order
list1.sort()
print(list1)
# Start Value in decending order
list1.sort(reverse=True)
print(list1)
# Give Index of given number
print(list1.index(3))
# Count How Many Times it appears in the list
print(list1.count(4))
# Not Recommened in Python
# m = list1
# m[0] = 0
# print(list1, m)
# Recommeneded:
m = list1.copy()
m[0] = 0
print(list1, m)
# Insert According to the Index
list1.insert(4, 333)
print(list1)
# Extend Method
u = [344, 221, 332, 44]
# it says place u List next to list1
list1.extend(u)
print(list1)
k = list1 + [33, 25, 55,22, 22, 11]
print(k)