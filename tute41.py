# os module creating directories
import os 

if(not os.path.exists("araiz")):
    os.mkdir("araiz")

for i in range(0, 100):
    os.mkdir(f"araiz/Day{i+1}")
