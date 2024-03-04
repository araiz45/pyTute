from plyer import notification
import time 
from datetime import datetime

def DrinkNotification(glass, time):
    notification.notify(
    title= f"Drink {glass} glass of water & take break",
    message=f"You should take break because it is {time}",
    app_icon= None,
    timeout=10,
    )
    return True

while True:
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%H:%M:%S")
    if currentTime == "07:01:01":
        condition = False
        condition = DrinkNotification(2, currentTime)
        time.sleep(2)
        if condition and (currentTime != "07:01:01"):
            continue
    elif currentTime == "09:01:01":
        condition = False
        condition = DrinkNotification(1, currentTime)
        time.sleep(2)
        if condition and (currentTime != "09:01:01"):
            continue
    elif currentTime == "12:01:01":
        condition = False
        condition = DrinkNotification(2, currentTime)
        time.sleep(2)
        if condition and (currentTime != "12:01:01"):
            continue
    elif currentTime == "15:01:01":
        condition = False
        condition = DrinkNotification(1, currentTime)
        time.sleep(2)
        if condition and (currentTime != "15:01:01"):
            continue
    elif currentTime == "20:57:00":
        condition = False
        condition = DrinkNotification(2, currentTime)
        time.sleep(2)
        if condition and (currentTime != "20:57:00"):
            continue
    else: 
        # print("nothing", currentTime, type(currentTime))
        pass




