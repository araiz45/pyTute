import time

currentTime = time.time()
currentTimeInTuple = time.localtime(currentTime)
currentHour = currentTimeInTuple.tm_hour

if(currentHour >= 6 and currentHour < 12):
    print("Good Mouring")
elif(currentHour >= 12 and currentHour < 16):
    print("Good Afternoon")
elif(currentHour >= 16 and currentHour < 20):
    print("Good Evening")
else:
    print("Good Night")
