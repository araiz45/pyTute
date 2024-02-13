# Break and Continue Statement

for i in range(12):
    if(i == 10):
        print('Skip the iteration')
        continue
    print("3 X", i, "=", 5*i)
    

for i in range(12):
    if(i == 10):
        # print('Skip the iteration')
        break
    print("3 X", i, "=", 5*i)
