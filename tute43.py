# os module listing directories
import os
folders = os.listdir("araiz")
print(folders)
print (os.getcwd())
os.chdir("C:/Users/anonymous/Desktop")
print(os.getcwd())

for folder in folders:
    print(folder)
    print(os.listdir(f"araiz/{folder}"))

