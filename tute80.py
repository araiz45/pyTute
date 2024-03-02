import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

listOfUser = ['Injir', 'Pista', 'Miswar', 'Paktwoon', 'Lal Baig', 'Misrey']

for user in listOfUser:
    print(f"Shout out to {user}")
    speaker.Speak(f"Shout out to {user}")

