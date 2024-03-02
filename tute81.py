import time
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def usingWhile():
    i = 0
    while i < 5000:
        print(i)
        i += 1

def usingFor():
    for i in range(5000):
        print(i)

# intialWhileTime = time.time()
# usingWhile()
# finalWhileTime = time.time() - intialWhileTime
# intialForTime = time.time()
# usingFor()
# finalForTime = time.time() - intialForTime

# if(finalWhileTime < finalForTime):
#     print('while wins')
#     print(f'while time: {finalWhileTime} | for time: {finalForTime} ')

# elif(finalForTime < finalWhileTime):
#     print('for wins')
#     print(f'while time: {finalWhileTime} | for time: {finalForTime} ')
# else:
#     print("tie")
#     print(f'while time: {finalWhileTime} | for time: {finalForTime} ')


# speaker.Speak("Going to wait for 4 seconds")
# time.sleep(4)
# speaker.Speak("Hello world")
        
intailizationOfTime = time.localtime()
formattedTime = time.strftime("%Y-%m-%d %H:%M:%S")

print(formattedTime)