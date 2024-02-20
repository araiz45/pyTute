# else with for loop 
for i in range(5):
    print(i)
else:
    print("Sorry no i")
# else will not execute
for i in range(10):
    if(i == 5):
        break
    print(i)
else:
    print("Sorry no i")

# while 
i = 0
while i < 7:
    print(i)
    if i == 4:
        break
    i = i + 1
else:
    print("sorry no i ")