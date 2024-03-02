import os 

listOfFiles = os.listdir("folder")

i = 1
indexOfItem = 0
while indexOfItem < len(listOfFiles):
    # print()
    os.rename(f"folder/{listOfFiles[indexOfItem]}", f"folder/{i}.txt")
    indexOfItem += 1
    i +=1
