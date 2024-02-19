name = "araiz"
fname = "zahid"
# F Strings
letter = f"Hey my name is {name} and my father name is {fname}"
print(letter)
# Older Version
letter2 = "Hy name is {} and my fname is {}"
naem = "Zahid"
fName = "Baig"
print(letter2.format(naem, fName))

letter2 = "Hy name is {1} and my fname is {0}"
naem = "Zahid"
fName = "Baig"
print(letter2.format(fName, naem))

# Take 2 decimal numbers
txt = "For only {price: .2f} dollars"
print(txt.format(price = 32.323445))

# By F-string take 2 decimal numbers
price = 2.3123445
txt = f"Only for dollar {price: .2f}"
print(txt)

print(f"{3*21}")


str1 = f"I'm showing how I use f string {{name}} and {{fname}}"
print(str1)