# Strings Methods in Python 
# Strings are immutuable - Means it cannot change
a = "araiz!!!!!!!!! is a good boy, and araiz is eating food"
# to find the lenght of the string
print(len(a))
# To make strings in uppercase
print(a.upper())
# To make strings in lowercase
print(a.lower())
# it will Print after striping ! from right
print(a.rstrip("!"))
# Replace - It will replace all occurances of the string to anther
print(a.replace("Araiz", "Injir"))
# it will convert string into list
print(a.split(" "))
# it will convert it into capitalize
print(a.capitalize())
# it will add space to make string center into the console
str1 = "Welcome to my blog"
print(str1.center(55))
# it will count how many times an given string is mention into the string
print(a.count("araiz"))
# tells if strings endswith certain string
str2 = "Welcome to my social app"
print(str2.endswith("app")) # True
print(str2.endswith("appt")) # False
# tells if certain string is their or not 
print(str1.endswith("to", 8, 10))
# it finds a certain string's first occurence and gives its index
print(str1.find("to"))
print(str1.find("hello")) # -1 cause it will not find
# this mehod is same as find but will raise error if it will not find it 
# print(str.index("issh"))
str1 = "HelloWorld123"
# It will return true if their is only numbers and alphabets
print(str1.isalnum())
# it will return true if their is only alphabets
str1 = "HelloWorld"
print(str1.isalpha()) 
# it will return lower if the case is in Lower case
print(str1.islower())
# it will return true if their is not a printable characher else false
print(str1.isprintable())
str1 = "hello world \n"
print(str1.isprintable())
# returns true if their is white spaces 
str1 = "Hellow rold "
print(str1.isspace())
# returns true if all the words in the strings starts with Capital letter
print(str1.istitle())
# returns true if certain string starts with given string 
print(str1.startswith("Hellow"))
# it will convert lowercase into upper and uppercase into lowercase
print (str1.swapcase())
# it will convert string into title case
print(str1.title())