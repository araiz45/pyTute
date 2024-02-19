# SET Methods 
sets = {1, 4, 24, 5, 2}
sets2 = {3, 5, 2}
# Union
print(sets.union(sets2))
# Update 
sets.update(sets2)
print(sets)

names = {"Pakistan", "Japan", "Canada", "Australia", "England"}
countries = {"Pakistan", "Japan", "Austria", "China", "America"}
# Intersection
print(names.intersection(countries))
# Intersection Update
names.intersection_update(countries)
print(names)

names = {"Pakistan", "Japan", "Canada", "Australia", "England"}
countries = {"Pakistan", "Japan", "Austria", "China", "America"}
# Symmetric difference
print(names.symmetric_difference(countries))
# Symmetric difference Update
names.symmetric_difference_update(countries)
print(names)

names = {"Pakistan", "Japan", "Canada", "Australia", "England"}
countries = {"Pakistan", "Japan", "Austria", "China", "America"}
# Difference
print(names.difference(countries))
# Difference Update
names.difference_update(countries)
print(names)

names = {"Pakistan", "Japan", "Canada", "Australia", "England"}
countries = {"Pakistan", "Japan", "Austria", "China", "America"}
# IsDisjoint Sets
print(names.isdisjoint(countries))

names = {"Pakistan", "Japan", "Canada", "Australia", "England"}
countries = {"Pakistan", "Japan", "Austria", "China", "America"}
# IsSuperSet Sets
print(names.issuperset(countries))

names = {"Pakistan", "Japan", "Canada", "Australia", "England"}
countries = {"Pakistan", "Japan", "Austria", "China", "America"}
# IsSubSet Sets
print(names.issubset(countries))

names = {"Pakistan", "Japan", "Canada", "Australia", "England"}
# Add
names.add("China")
print(names)

names = {"Pakistan", "Japan", "Canada", "Australia", "England"}
# Remove
names.remove("Pakistan")
print(names)

names = {"Pakistan", "Japan", "Canada", "Australia", "England"}
# Discard - It does not returns error 
names.discard("Pakistan")
print(names)

names = {"Pakistan", "Japan", "Canada", "Australia", "England"}
# POP - Remove last Item from the set 
item = names.pop()
print(item)
print(names)

names = {"Pakistan", "Japan", "Canada", "Australia", "England"}
# Del - Remove all the set
del names
# print(names)

names = {"Pakistan", "Japan", "Canada", "Australia", "England"}
# Clear - Clear all the set
names.clear()
print(names)


names = {"Pakistan", "Japan", "Canada", "Australia", "England"}
# Clear - Clear all the set
if "Pakistan" in names:
    print("yes")
else:
    print("No")