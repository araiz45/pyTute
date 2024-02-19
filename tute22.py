# Tuples
tup = (1, 4, 5)
# for one list item
tup1 = (1,)
print(tup1, tup)
# Tuples are immutables
multiTup = (3, 5, "Hello", True)
print(multiTup)
print(multiTup[3])
print(multiTup[-2])
# Check item exist in tuple
if "Hello" in multiTup:
    print("Yes Present")

# Making new Tuple using slicing
multiTup2 = multiTup[1: 3]
print(multiTup2)