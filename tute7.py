# String Slicing and Operators on Strings
names = "araiz, injir, pashto, kundi"
# to find the lenght of the string
print(len(names))
# slicing 
print(names[0: 5]) # including 0 but not 5
print(names[1: 4]) # including 1 but not 4
print(names[: 4])
# Negative slicing
print(names[: -4])
print(names[: len(names)-4])
print(names[-1: -5])
print(names[-5: -1])
print(names[-5: ])
# Quick Quiz
nm = "Harry"
print(nm[-4:-2])
