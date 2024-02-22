# file handling
# Read
f = open ('human.js', 'r')
text = f.read()
print(text)
f.close()
# Write 
f = open ('human.js', 'w')
textIn = input("Enter you want to write: ")
text = f.write(textIn)
f.close()
# Read bytses;
f = open ('human.js', 'rb')
text = f.read()
print(text)
f.close()
# Appand
f = open ('human.js', 'a')
textIn = input("Enter you want to write: ")
text = f.write(textIn)
f.close()